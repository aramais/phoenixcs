from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader, Template
from extreg.models import preliminaryRegistration, preliminaryRegistrationForm
# Create your views here.


def viewExtReg(request):
	if request.method == 'POST':
		form = preliminaryRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('OKEY')
		else:
			return render(request, 'extreg/reg_mer_form.html', {'form':form})
	else:
		form = preliminaryRegistrationForm({})
		return render(request, 'extreg/reg_mer_form.html', {'form':form})

def polotno(request):
	form = preliminaryRegistrationForm()
	return render(request, 'extreg/polotno.html', {'form':form})
