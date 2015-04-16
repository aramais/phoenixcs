from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader, Template
from myarticle.models import DefaultArticle, DefaultTag, TagEdge

def listArticles(request):
	#context = RequestContext(request, {'articles': DefaultArticle.objects.all()})
	#context = RequestContext(request)
	return render(request, 'myarticle/articleslist.html', {'articles': DefaultArticle.objects.all()})
	
def detailedArticle(request, article_id):
	article = get_object_or_404(DefaultArticle, id = article_id)
	#context = RequestContext(request)
	#context = RequestContext(request, {'thearticle': article})
	return render_to_response('myarticle/thearticle.html', {'thearticle': article}, RequestContext(request))
	#return render(request, 'myarticle/thearticle.html', {'thearticle': article})
	
def detailedArticleByUrl(request, article_url):
	article = get_object_or_404(DefaultArticle, url = article_url)
	#context = RequestContext(request)
	#context = RequestContext(request, {'thearticle': article})
	return render_to_response('myarticle/thearticle.html', {'thearticle': article}, RequestContext(request))
	#return render(request, 'myarticle/thearticle.html', {'thearticle': article})
	
def listByTag(request, tag_id):
	tag = DefaultTag.objects.get(id = tag_id)
	articles = [edge.article for edge in tag.tagedge_set.all()]
	return render(request, 'myarticle/articlesbytag.html', {'articles': articles, 'tag':tag})
	
def listByTagText(request, tag_text):
	tag = DefaultTag.objects.get(text = tag_text)
	articles = [edge.article for edge in tag.tagedge_set.all()]
	return render(request, 'myarticle/articlesbytag.html', {'articles': articles, 'tag':tag})