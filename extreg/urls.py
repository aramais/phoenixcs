from django.conf.urls import patterns, url
from extreg import views

urlpatterns = patterns('',
	url(r'^reg_form_event', views.viewExtReg, name = 'viewExtReg'),
	url(r'^polotno', views.polotno, name = 'polotno'),
)
