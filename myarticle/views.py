from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from myarticle.models import DefaultArticle, DefaultTag, TagEdge

def listArticles(request):
	#context = RequestContext(request, {'articles': DefaultArticle.objects.all()})
	#context = RequestContext(request)
	return render(request, 'myarticle/articleslist.html', {'articles': DefaultArticle.objects.all()})
	
def detailedArticle(request, article_id):
	article = get_object_or_404(DefaultArticle, id = article_id)
	#context = RequestContext(request)
	#context = RequestContext(request, {'thearticle': article})
	return render(request, 'myarticle/thearticle.html', {'thearticle': article})
	
def listByTag(request, tag_id):
	tag = DefaultTag.objects.get(id = tag_id)
	articles = [edge.article for edge in tag.tagedge_set.all()]
	return render(request, 'myarticle/articlesbytag.html', {'articles': articles, 'tag':tag})