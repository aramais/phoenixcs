# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

from myarticle.views import newsIndex

urlpatterns = patterns('',
    # Examples:
    url(r'^accounts/', include('userena.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'phoenixcs.views.home', name='home'),
	url(r'^$', newsIndex, name='home'),
    # url(r'^blog/', include('blog.urls')),
	#url(r'^articles/', include('myarticle.urls', namespace = 'myarticle')),
	url(r'^news/', include('myarticle.urls', namespace = 'myarticle')),
	#url(r'^admin_tools/', include('admin_tools.urls')), #balovstvo odno tol'ko!
	url(r'^redactor/', include('redactor.urls')),
	url(r'^comments/', include('django_comments.urls')),
	url(r'^blog/comments/', include('fluent_comments.urls')),
	url(r'^messages/', include('userena.contrib.umessages.urls')),
)
