from django.conf.urls import patterns, url
from myarticle import views

urlpatterns = patterns('',
	url(r'^$', views.listArticles, name = 'listArticles'),
	#url(r'^(?P<article_id>\d+)/$', views.detailedArticle, name='detailedArticle'),
	#url(r'^tag/(?P<tag_id>\d+)/$', views.listByTag, name='listByTag'),
	url(r'^category/(?P<category_id>\d+)/$', views.listByCategory, name='listByCategory'),
	url(r'^article/(?P<article_url>\w+)', views.detailedArticleByUrl, name='detailedArticleByUrl'),
	url(r'^tag/(?P<tag_text>\w+)', views.listByTagText, name='listByTagText'),
)