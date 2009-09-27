from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # main page
    url(r'^$', 'apps.mapper.views.index', name='index'),

    
)