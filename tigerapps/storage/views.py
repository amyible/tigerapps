import sys, os
import uuid
from os import path
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.conf import settings
from django_cas.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from storage.forms import *
from storage.models import *
from paypal import standard
from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard import ipn
from paypal.standard.ipn import views
from paypal.standard.ipn.signals import payment_was_successful
from paypal.standard.ipn.signals import payment_was_flagged
from django.core.mail import send_mail
from django.dispatch import receiver

def home(request):
    postList = Post.objects.all().order_by('posted').reverse()
    paginator = Paginator(postList, 3)
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    # If page # is out of range, deliver 1st page of results.
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(1)
        
    return render_to_response('storage/index.html', 
                              {'posts': posts},
                              RequestContext(request))

@login_required
def register(request):
    #XXX: close registration
    return HttpResponseRedirect('/register/closed/')

    #Make sure user didn't already register
    try:    
        status = Order.objects.get(user=request.user)
        return HttpResponseRedirect('/order/')
    except:
        pass
    
    #Get the list of dropoffpickuptimes
    dp_qset = DropoffPickupTime.objects.all()
    tmp = [str(x).split(', ') for x in dp_qset]
    dp_times = [(str(x.id),
                 y[0],
                 y[1],
                 y[2],
                 x.n_boxes_total-x.n_boxes_bought) for x,y in zip(dp_qset,tmp)]
    
    #Process the user's input if POST
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if not reg_form.is_valid():
            try:    c = request.POST['dropoff_pickup_time']
            except: c = None
            return render_to_response('storage/register_1_info.html',
                                      {'reg_form': reg_form,
                                       'box_price': reg_form.BOX_PRICE,
                                       'max_boxes': reg_form.MAX_BOXES,
                                       'dp_choice': c,
                                       'dp_times': dp_times},
                                      RequestContext(request))
        form = reg_form.save(request.user, commit=True)
        
        #Render data to show on next page
        unpaid_order = UnpaidOrder.objects.get(invoice_id=form.invoice_id)
        reg_info = ((0, 'NetID:', request.user.username),
                    (0, 'Email:', request.user.username+'@princeton.edu'),
                    (0, 'Cell phone number*:', unpaid_order.cell_number),
                    (1, 'Dropoff/pickup time*:', str(unpaid_order.dropoff_pickup_time).split(', ')),
                    (0, 'Price per box:', '$'+reg_form.BOX_PRICE),
                    (0, 'Quantity (max %d)*:'%reg_form.MAX_BOXES, unpaid_order.n_boxes_bought),
                    (0, 'Total price:', '$%.2f'%(float(reg_form.BOX_PRICE)*unpaid_order.n_boxes_bought)),
                    (0, ' ', ' '),
                    (0, 'Proxy name:', unpaid_order.proxy_name),
                    (0, 'Proxy email:', unpaid_order.proxy_email))
        pp_details = {
            'business': 'agencies@princeton.edu',
            #'business': 'it@princetonusg.com',
            'item_name': "USG summer storage boxes",
            'item_number': "box",
            'amount': reg_form.BOX_PRICE,
            'quantity': unpaid_order.n_boxes_bought,
            
            'invoice': unpaid_order.invoice_id,
            'notify_url': settings.SITE_DOMAIN+'/paypal/ipntesturl123/',
            'return_url': settings.SITE_DOMAIN+'/register/complete/',
            'cancel_return': settings.SITE_DOMAIN+'/register/',
        }
        pp_form = PayPalPaymentsForm(initial=pp_details)
        #pp_form_rendered = pp_form.sandbox()
        pp_form_rendered = pp_form.render()
        return render_to_response('storage/register_2_paypal.html',
                                  {'reg_info': reg_info,
                                   'pp_info': pp_form_rendered},
                                  RequestContext(request))
    
    #Return empty form if GET
    reg_form = RegistrationForm()
    return render_to_response('storage/register_1_info.html',
                              {'reg_form': reg_form,
                               'box_price': reg_form.BOX_PRICE,
                               'max_boxes': reg_form.MAX_BOXES,
                               'dp_times': dp_times},
                              RequestContext(request))

@login_required
def register_complete(request):
    return render_to_response('storage/register_3_complete.html',
                              {},
                              RequestContext(request))

@login_required
def order(request):
    try:
        order = Order.objects.get(user=request.user)
    except:
        return render_to_response('storage/order.html',
                                  {},
                                  RequestContext(request))

    #render the form, or update the form if a POST
    if request.method == 'POST':
        form = ProxyUpdateForm(request.POST)
        if form.is_valid():
            form.save(order)
    form = ProxyUpdateForm()
    
    #render the other info
    reg_info = ((0, 'NetID:', request.user.username),
                (0, 'Email:', request.user.username+'@princeton.edu'),
                (0, 'Cell phone number:', order.cell_number),
                (1, 'Dropoff/pickup time:', str(order.dropoff_pickup_time).split(', ')),
                (0, 'Box size:', '18"x18"x17"'),
                (0, 'Price per box:', '$'+RegistrationForm.BOX_PRICE),
                (0, 'Quantity:', order.n_boxes_bought),
                (0, 'Total paid:', '$%.2f'%(float(RegistrationForm.BOX_PRICE)*order.n_boxes_bought)))
    proxy_info = (order.proxy_name, order.proxy_email)
    
    return render_to_response('storage/order.html',
                              {'reg_info': reg_info,
                               'proxy_info': proxy_info,
                               'proxy_form': form},
                              RequestContext(request))
@login_required
@user_passes_test(lambda u: u.is_staff)
def emails(request):
    orders = Order.objects.all()
    order_emails = set(order.user.username + '@princeton.edu' for order in orders)
    unpaid_orders = UnpaidOrder.objects.all()
    unpaid_order_emails = set(u_order.user.username + '@princeton.edu' for u_order in unpaid_orders if u_order.user.username+'@princeton.edu' not in order_emails)
    return render_to_response('storage/emails.html', {'u_orders': unpaid_order_emails, 'orders': order_emails}, RequestContext(request))


#------------------
#paypal stuff
#------------------

def my_ipn(request):
    try:
        send_mail('my_ipn', 'in my_ipn', 'from@example.com', ['mfrankli@princeton.edu'], fail_silently=False)
        toReturn = ipn.views.ipn(request)
        payment_was_successful.connect(confirm_payment)
        return toReturn
    except Exception as e:
        send_mail('my_ipn', str(e), 'from@example.com', ['mfrankli@princeton.edu'], fail_silently=False)
        return HttpResponse('OKAY')

def confirm_payment(sender, **kwargs):
    # make Order, put in db
    # look for invoice_id
    try:
        send_mail('confirm_payment', str(sender), 'from@example.com', ['mfrankli@princeton.edu'], fail_silently=False)
        unpaid_order = UnpaidOrder.objects.get(invoice_id=sender.invoice)
        dropoff_pickup_time = unpaid_order.dropoff_pickup_time
        dropoff_pickup_time.n_boxes_bought += unpaid_order.n_boxes_bought
        dropoff_pickup_time.save()
        order = Order(user=unpaid_order.user,
                      cell_number=unpaid_order.cell_number,
                      dropoff_pickup_time=unpaid_order.dropoff_pickup_time,
                      proxy_name=unpaid_order.proxy_name,
                      proxy_email=unpaid_order.proxy_email,
                      n_boxes_bought=unpaid_order.n_boxes_bought,
                      invoice_id=unpaid_order.invoice_id,
                      signature=unpaid_order.signature)
        order.save()        
    except Exception as e:
        send_mail('confirm_payment', 'something went wrong sending: ' + str(e), 'from@example.com', ['mfrankli@princeton.edu'], fail_silently=False)

payment_was_successful.connect(confirm_payment)

def handle_flagged(sender, **kwargs):
    send_mail('Subject here', 'Here is the message. (Flagged!)', 'from@example.com',
              ['mfrankli@princeton.edu'], fail_silently=False)

payment_was_flagged.connect(handle_flagged)
