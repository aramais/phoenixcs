from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader, Template
from myarticle.models import Article, Tag, TagEdge, Category
from endless_pagination.decorators import page_template

def getCategoriesList():
	return [{'category':category, 'narticles':len([a for a in category.article_set.all() if a.visible])} for category in Category.objects.all()]
	
@page_template('myarticle/articleswidget.html') 
def listArticles(request, template = 'myarticle/articleslist.html', category_id = None, tag_text = None, extra_context = None):
	context = {'cats':getCategoriesList()}
	if tag_text:
		tag = Tag.objects.get(text = tag_text)
		articles = [edge.article for edge in tag.tagedge_set.all()]
		template = 'myarticle/articlesbytag.html'
		context['tag'] = tag
	elif category_id:
		category = Category.objects.get(id = category_id)
		articles = [a for a in category.article_set.all()]
		template = 'myarticle/articlesbycategory.html'
		context['category'] = category
	else:
		articles = [a for a in Article.objects.all()]
	articles = [a for a in articles if a.visible]
	context['articles'] = articles
	if extra_context is not None:
        	context.update(extra_context)
	return render_to_response(template, context, RequestContext(request))
	
def detailedArticleByUrl(request, article_url):
	article = get_object_or_404(Article, url = article_url)
	return render_to_response('myarticle/thearticle.html', {'thearticle': article, 'cats':getCategoriesList()}, RequestContext(request))
	
def newsIndex(request):
	return render(request, 'myarticle/newsindex.html', {'articles': [a for a in Article.objects.all() if a.visible]})
