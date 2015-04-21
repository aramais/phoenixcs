from django.conf.urls import patterns, url
from myarticle import views

urlpatterns = patterns('',
	url(r'^$', views.listArticles, name = 'listArticles'),
	url(r'^category/(?P<category_id>\d+)/$', views.listArticles, name='listByCategory'),
	url(r'^tag/(?P<tag_text>\w+)', views.listArticles, name='listByTagText'),
	#url(r'^category/(?P<category_id>\d+)/$', views.listByCategory, name='listByCategory'),
	#url(r'^tag/(?P<tag_text>\w+)', views.listByTagText, name='listByTagText'),
	url(r'^(?P<article_url>\w+)', views.detailedArticleByUrl, name='detailedArticleByUrl'),
)
