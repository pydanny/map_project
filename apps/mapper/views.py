# Create your views here.
import datetime

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django.utils.translation import ugettext_lazy as _
from django.views.generic import date_based


from apps.mapper.models import ApplicationType, Application, Mapp

def index(request, template_name="mapper/index.html"):
    applications = Application.objects.all()
    
    return render_to_response(template_name, {
        "applications": applications,
    }, context_instance=RequestContext(request))

