# Create your views here.
import datetime

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.defaultfilters import slugify


from django.utils.translation import ugettext_lazy as _
from django.views.generic import date_based

import pygraphviz as pgv

from apps.mapper.models import Application, Mapp
from apps.graphviz.helpers import create_graph

def index(request, template_name="mapper/index.html"):
    applications = Application.objects.all()
    return render_to_response(template_name, {
        "applications": applications,
    }, context_instance=RequestContext(request))

def get_app(application_id):
    try:
        application = Application.objects.get(title = application_id)
    except Application.DoesNotExist:
        application = get_object_or_404(Application, id = application_id)
    return application

def application(request, application_id, template_name="graphviz/application.html"):
    
    application = get_app(application_id)
    
    return render_to_response(template_name, {
        "application": application,
    }, context_instance=RequestContext(request))
    
def make_node(graph, application):
    
    slug_title = slugify(application.title)    
    graph.add_node(slug_title)
    node = graph.get_node(slug_title)
    node.attr['shape'] = str(application.application_type.shape)
    node.attr['color'] = str(application.application_type.color)
    node.attr['label'] = str(application.title)
    node.attr['link'] = str(slug_title)    
    return graph
    

def application_image(request, application_id, format):
    
    application = get_app(application_id)
    slug_app_title = slugify(application.title)     

    graph = pgv.AGraph(strict=False,directed=True)
    graph.graph_attr['label'] = 'Map for %s' % str(application.title)
    graph.node_attr['shape'] = 'box'

    graph = make_node(graph, application)
    
    for app in application.pulling():

        graph = make_node(graph, app)        
        graph.add_edge(slugify(app.title), slug_app_title)        

    for app in application.pushing():

        graph = make_node(graph, app)        
        graph.add_edge(slug_app_title, slugify(app.title))

    image = create_graph(graph.string())
    
    return HttpResponse(image, mimetype="image/gif")
    