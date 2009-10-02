# Create your views here.

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.template import RequestContext

from xlwt import Workbook
from tempfile import TemporaryFile

from apps.mapper.models import Application

def index(request):
    
    book = Workbook()
    app_sheet = book.add_sheet('Applications')
    app_sheet.write(0, 0, "Application")
    app_sheet.write(0, 1, "Type")
    
    for index, app in enumerate(Application.objects.all().order_by('title')):
        row = app_sheet.row(index+2)
        row.write(0, app.title)
        row.write(1, app.application_type.title)    
        
    book.save('simple.xls')
    book.save(TemporaryFile())
    report = open('simple.xls','rb').read()
    return HttpResponse(report, mimetype="application/vnd.ms-excel")  