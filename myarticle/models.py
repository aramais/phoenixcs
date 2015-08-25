# -*- coding: utf-8 -*-
# русские коменты
from django.db import models
from datetime import date
from django.core.urlresolvers import reverse
from django.utils import timezone

class Category(models.Model):
	text = models.CharField(max_length=200, default = "Not categorized")
	def __unicode__(self):
		#return '<Article Category "' + str(self.id) + '">'
		return '<Article Category "' + self.text + '">'

class Article(models.Model):
	title = models.CharField(max_length=200)
	url = models.SlugField(max_length=50, unique = True)
	text = models.TextField()
	image = models.ImageField(upload_to='images', default = 'images/default.jpg')
	date = models.DateField(default = timezone.now)
	author = models.CharField(max_length=200, default = "author unknown")
	category = models.ForeignKey(Category, default = 0)
	visible = models.BooleanField(default = False)
	def __unicode__(self):
		#return '<Article "' + str(self.id) + '">'
		return '<Article "' + self.title + '">'
	def get_absolute_url(self):
		#hardcoded url!!! need to use 'reverse', but problems with cyclical import
		return '/news/' + self.url

class Tag(models.Model):
	text = models.CharField(max_length=200, unique = True)
	#parent = models.ForeignKey(Tag)
	def __unicode__(self):
		return '<Tag "' + self.text + '">'

class TagEdge(models.Model):
	article = models.ForeignKey(Article)
	tag = models.ForeignKey(Tag)
	def __unicode__(self):
		#return '<Tag-Article pair "' + str(self.article.id) + '"-"' + str(self.tag.id) + '">'
		return '<Tag-Article pair "' + self.article.title + '"-"' + self.tag.text + '">'
