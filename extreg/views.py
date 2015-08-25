from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader, Template
from extreg.models import preliminaryRegistration, preliminaryRegistrationForm
# Create your views here.


def viewExtReg(request):
	if request.method == 'POST':
		form = preliminaryRegistrationForm(request.POST)
		tmp = form.is_valid()
		request.session['registration_form_data'] = form.cleaned_data
		if form.is_valid():
			form.save()
			return HttpResponse('OKEY')
		else:
			return render(request, 'extreg/reg_mer_form.html', {'form':form})
	else:
		form = preliminaryRegistrationForm({})
		if 'registration_form_data' in request.session:
			form = preliminaryRegistrationForm(request.session['registration_form_data'])
		return render(request, 'extreg/reg_mer_form.html', {'form':form})

def polotno(request):
	if request.method == 'POST':
		form = preliminaryRegistrationForm(request.POST)
		tmp = form.is_valid()
		request.session['registration_form_data'] = form.cleaned_data
	else:
		form = preliminaryRegistrationForm()
	seen = 0
	if 'registration_form_data' in request.session:
			seen = 1
			form = preliminaryRegistrationForm(request.session['registration_form_data'])
	return render(request, 'extreg/polotno.html', {'form':form, 'seen': seen})
