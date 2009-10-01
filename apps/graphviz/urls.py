from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # main image
    url(r'^$', 'apps.graphviz.views.index', name='graphviz_index'),
    
    # blog post for user
    url(r'^(?P<application_id>\w+)\.(?P<format>\w+)$', 'apps.graphviz.views.application_image', 
                name='graphviz_application_image'),        
    url(r'^(?P<application_id>\w+)/$', 'apps.graphviz.views.application', name='graphviz_application'),


    
)