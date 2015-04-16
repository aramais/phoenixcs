from django.db import models

class DefaultArticle(models.Model):
	title = models.CharField(max_length=200)
	url = models.SlugField(max_length=50, unique = True)
	text = models.TextField()
	image = models.ImageField(upload_to='images')
	def __str__(self):
		return '<Article "' + self.title + '">'

class DefaultTag(models.Model):
	text = models.CharField(max_length=200, unique = True)
	#parent = models.ForeignKey(DefaultTag)
	def __str__(self):
		return '<Tag "' + self.text + '">'

class TagEdge(models.Model):
	article = models.ForeignKey(DefaultArticle)
	tag = models.ForeignKey(DefaultTag)
	def __str__(self):
		return '<Tag-Article pair "' + self.article.title + '"-"' + self.tag.text + '">'