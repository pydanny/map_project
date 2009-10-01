from django.conf.urls.defaults import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^', include('apps.mapper.urls')),
    (r'^graphviz/', include('apps.graphviz.urls')),    

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
