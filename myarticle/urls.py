from django.conf.urls import patterns, url
from myarticle import views

urlpatterns = patterns('',
	url(r'^$', views.listArticles, name = 'listArticles'),
	url(r'^(?P<article_id>\d+)/$', views.detailedArticle, name='detailedArticle'),
	url(r'^tag/(?P<tag_id>\d+)/$', views.listByTag, name='listByTag'),
)