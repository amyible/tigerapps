import uuid
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from django_cas.decorators import login_required, user_passes_test
from paypal.standard.forms import PayPalPaymentsForm
from storage.forms import RegistrationForm

@login_required
def register(request):
    if request.method == 'POST':
        status_form = RegistrationForm(request.POST)
        if status_form.is_valid():
            log = status_form.save(request.user, commit=True)
            return render_to_response('storage/registration_complete.html')
        
    status_form = RegistrationForm()
    netid = request.user
    
    #adam's shit
    title = "Box"
    price = 9.40
    quantity = 2
    paypal = {
        'amount': price,
        'item_name': "Box",
        'item_number': "box",
        'quantity': quantity,
        
        # PayPal wants a unique invoice ID
        'invoice': str(uuid.uuid1()), 
        
        # It'll be a good idea to setup a SITE_DOMAIN inside settings
        # so you don't need to hardcode these values.
        'return_url': settings.SITE_DOMAIN,
        'cancel_return': settings.SITE_DOMAIN,
    }
    form = PayPalPaymentsForm(initial=paypal)
    if settings.DEBUG:
        rendered_form = form.sandbox()
    else:
        rendered_form = form.render()

    #render the template
    return render_to_response('storage/register.html',
                              {'registration_form': status_form, 'user_netid': netid,           
                               'title' : title,
                              'price' : price,
                               'form' : rendered_form,
                               'quantity': quantity,},
                              RequestContext(request))
                          

def product_detail(request):
    title = "Box"
    price = 9.40
    quantity = 2
    paypal = {
        'amount': price,
        'item_name': "Box",
        'item_number': "box",
        'quantity': quantity,
        
        # PayPal wants a unique invoice ID
        'invoice': str(uuid.uuid1()), 
        
        # It'll be a good idea to setup a SITE_DOMAIN inside settings
        # so you don't need to hardcode these values.
        'return_url': settings.SITE_DOMAIN,
        'cancel_return': settings.SITE_DOMAIN,
    }
    form = PayPalPaymentsForm(initial=paypal)
    if settings.DEBUG:
        rendered_form = form.sandbox()
    else:
        rendered_form = form.render()
    return render_to_response('storage/paypal.html', {
        'title' : title,
        'price' : price,
        'form' : rendered_form,
    }, RequestContext(request))
