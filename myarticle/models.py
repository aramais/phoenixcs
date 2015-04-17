from django.db import models
from datetime import date

class Category(models.Model):
	text = models.CharField(max_length=200, default = "Not categorized")
	def __str__(self):
		return '<Article Category "' + self.text + '">'

class Article(models.Model):
	title = models.CharField(max_length=200)
	url = models.SlugField(max_length=50, unique = True)
	text = models.TextField()
	image = models.ImageField(upload_to='images')
	date = models.DateField(default = date.today())
	author = models.CharField(max_length=200, default = "author unknown")
	category = models.ForeignKey(Category, default = 0)
	visible = models.BooleanField(default = False)
	def __str__(self):
		return '<Article "' + self.title + '">'

class Tag(models.Model):
	text = models.CharField(max_length=200, unique = True)
	#parent = models.ForeignKey(Tag)
	def __str__(self):
		return '<Tag "' + self.text + '">'

class TagEdge(models.Model):
	article = models.ForeignKey(Article)
	tag = models.ForeignKey(Tag)
	def __str__(self):
		return '<Tag-Article pair "' + self.article.title + '"-"' + self.tag.text + '">'
