from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # TigerTrade
    (r'^admin/', include(admin.site.urls)),
    (r'^/?$', 'ccc.views.index'),
    url(r'^about/?$', 'ccc.views.post', kwargs={'postTitle': "About"}),
    url(r'^blog/?$', 'ccc.views.blog'),
<<<<<<< HEAD
=======
    url(r'^top/?$', 'ccc.views.top'),
    url(r'^all_hours/?$', 'ccc.views.all_hours'),
>>>>>>> 1994cf8d56d0192da28cf65baa61dffc0640b457
    url(r'^thankyou/?$', 'ccc.views.post', kwargs={'postTitle': "\"Thank You\"s"}),
    #url(r'^logging/?$', 'ccc.views.post', kwargs={'postTitle': "Logging"}),
    #url(r'^log-test/?$', 'ccc.views.log_choices'),
    url(r'^log/?$', 'ccc.views.log_hours'),
    url(r'^request/?$', 'ccc.views.project_request'),
    url(r'^contact/?$', 'ccc.views.post', kwargs={'postTitle': "Contact Us"}),
    url(r'^register/?$', 'ccc.views.post', kwargs={'postTitle': "Register"}),
    url(r'^opportunities/?$', 'ccc.views.post', kwargs={'postTitle': "Find an Opportunity!"}),
    
    # Admin
    (r'^login/?$', 'django_cas.views.login'),
    (r'^logout/?$', 'django_cas.views.logout'),
    
    # Try to find a post called that
    url(r'^(?P<postTitle>\w+)/?$', 'ccc.views.post'),
)