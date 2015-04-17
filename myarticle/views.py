from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader, Template
from myarticle.models import Article, Tag, TagEdge, Category

def getCategoriesList():
	return [{'category':category, 'narticles':len([a for a in category.article_set.all() if a.visible])} for category in Category.objects.all()]
	

def listArticles(request):
	return render(request, 'myarticle/articleslist.html', {'articles': [a for a in Article.objects.all() if a.visible], 'cats':getCategoriesList()})
	
def detailedArticle(request, article_id):
	article = get_object_or_404(Article, id = article_id)
	return render_to_response('myarticle/thearticle.html', {'thearticle': article, 'cats':getCategoriesList()}, RequestContext(request))
	
def detailedArticleByUrl(request, article_url):
	article = get_object_or_404(Article, url = article_url)
	return render_to_response('myarticle/thearticle.html', {'thearticle': article, 'cats':getCategoriesList()}, RequestContext(request))
	
def listByTag(request, tag_id):
	tag = Tag.objects.get(id = tag_id)
	articles = [edge.article for edge in tag.tagedge_set.all() if edge.article.visible]
	return render(request, 'myarticle/articlesbytag.html', {'articles': articles, 'tag':tag, 'cats':getCategoriesList()})
	
def listByTagText(request, tag_text):
	tag = Tag.objects.get(text = tag_text)
	articles = [edge.article for edge in tag.tagedge_set.all()]
	return render(request, 'myarticle/articlesbytag.html', {'articles': articles, 'tag':tag, 'cats':getCategoriesList()})
	
def listByCategory(request, category_id):
	category = Category.objects.get(id = category_id)
	articles = [a for a in category.article_set.all() if a.visible]
	return render(request, 'myarticle/articlesbycategory.html', {'articles': articles, 'category':category, 'cats':getCategoriesList()})
	
def newsIndex(request):
	return render(request, 'myarticle/newsindex.html', {'articles': [a for a in Article.objects.all() if a.visible]})
