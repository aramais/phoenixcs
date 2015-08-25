# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.forms import EditProfileFormExtra1
from myarticle.views import newsIndex
from views import landing_page

urlpatterns = patterns('',
    # Examples:
    url(r'^accounts/(?P<username>[\@\.\w-]+)/edit/$',  'userena.views.profile_edit', {'edit_profile_form': EditProfileFormExtra1},name='userena_profile_edit'),
    url(r'^accounts/(?P<username>[\@\.\w-]+)/edit/extra/$',  'accounts.views.profile_edit_extended',name='profile_edit_extended'),
    url(r'^accounts/(?P<username>[\@\.\w-]+)/cv/$',  'accounts.views.profile_detail_extended',name='cv'),
    url(r'^accounts/', include('userena.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'phoenixcs.views.home', name='home'),
	#url(r'^$', newsIndex, name='home'),
	url(r'^$', landing_page, name='home'),
    # url(r'^blog/', include('blog.urls')),
	#url(r'^articles/', include('myarticle.urls', namespace = 'myarticle')),
	url(r'^news/', include('myarticle.urls', namespace = 'myarticle')),
	#url(r'^admin_tools/', include('admin_tools.urls')), #balovstvo odno tol'ko!
	url(r'^redactor/', include('redactor.urls')),
	url(r'^comments/', include('django_comments.urls')),
	url(r'^blog/comments/', include('fluent_comments.urls')),
	url(r'^messages/', include('userena.contrib.umessages.urls')),
	url(r'^registration/', include('extreg.urls')),
)
