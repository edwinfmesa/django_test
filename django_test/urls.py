from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
from first_app.views import mostrar, home
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home),
    url(r'^blog/$', mostrar),
#    ('', mostrar),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)



# tus urlpatterns de toda la vida
#
#if settings.DEBUG and settings.STATIC_ROOT:
#    urlpatterns += patterns('',
#        (r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), 
#            'django.views.static.serve',
#            {'document_root' : settings.STATIC_ROOT }),)
#    
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )