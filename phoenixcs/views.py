from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render, render_to_response, redirect

def home(request):
    template=loader.get_template('index.html')
    context = RequestContext(request, {}) #'latest_question_list': latest_question_list,
    return HttpResponse(template.render(context))

def landing_page(request):
	template=loader.get_template('landing_page.html')
	context = RequestContext(request, {}) 
	return HttpResponse(template.render(context))
