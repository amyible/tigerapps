from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/?$', 'elections.views.home', name='home'),
    (r'^login/?', 'django_cas.views.login'),
    (r'^logout/?', 'django_cas.views.logout'),
    (r'^remove/?$', 'elections.views.remove'),
    #(r'^runoff/?$', 'elections.views.runoff'),
    url(r'^register/?$', 'elections.views.signup', kwargs={'election': None}),
    url(r'^statements/?$', 'elections.views.statements', name='statements'),

    # Admin
    url(r'^admin/?$', 'django_cas.views.login', kwargs={'next_page': '/djadmin/'}),
    (r'^djadmin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

