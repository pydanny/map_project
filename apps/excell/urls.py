from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # main page
    url(r'^report.xls$', 'apps.excell.views.index', name='excel_report'),

    
)