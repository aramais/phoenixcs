from django.conf.urls import patterns, url
from myarticle import views

urlpatterns = patterns('',
	url(r'^$', views.listArticles, name = 'listArticles'),
	url(r'^category/(?P<category_id>\d+)/$', views.listArticles, name='listByCategory'),
	url(r'^tag/(?P<tag_text>\w+)', views.listArticles, name='listByTagText'),
	url(r'^deletecomment/(?P<comment_id>\d+)', views.delete_my_comment, name = 'deleteMyComment'),
	url(r'^atp', views.ajaxTestPage, name='atp'),
	url(r'^ato', views.ajaxTestOk, name='ato'),
	url(r'^(?P<article_url>\w+)', views.detailedArticleByUrl, name='detailedArticleByUrl'),
)
