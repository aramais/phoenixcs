from django.db import models

class DefaultArticle(models.Model):
	title = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	text = models.CharField(max_length=5000)
	def __str__(self):
		return '<Article "' + self.title + '">'

class DefaultTag(models.Model):
	text = models.CharField(max_length=200)
	#parent = models.ForeignKey(DefaultTag)
	def getTags(self):
		return TagEdge.objects.get(article = self)
	def __str__(self):
		return '<Tag "' + self.text + '">'

class TagEdge(models.Model):
	article = models.ForeignKey(DefaultArticle)
	tag = models.ForeignKey(DefaultTag)
	def __str__(self):
		return '<Tag-Article pair "' + self.article.title + '"-"' + self.tag.text + '">'