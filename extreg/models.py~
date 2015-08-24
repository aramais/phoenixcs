# coding:utf-8
from django.db import models
from django.forms import ModelForm

# Create your models here.

class preliminaryRegistration(models.Model):
	surname = models.CharField(u'Фамилия', max_length=200)
	name = models.CharField(u'имя', max_length=200)
	thirdname = models.CharField(u'Отчество', max_length=200)
	email = models.CharField(u'Электронная почта', max_length=200)
	phone = models.CharField(u'Контактный телефон', max_length=200)
	university = models.CharField(u'Университет', max_length=200)
	faculty = models.CharField(u'Факультет', max_length=200, null = True)
	course = models.CharField(u'Курс', max_length=200, null = True)
	dateEntry = models.DateTimeField(auto_now=True)



# Create the form class.
class preliminaryRegistrationForm(ModelForm):
	class Meta:
		model = preliminaryRegistration
		exclude = ['dateEntry']
	def __init__(self, *args, **kwargs):
		# first call parent's constructor
		super(preliminaryRegistrationForm, self).__init__(*args, **kwargs)
		# there's a `fields` property now
		self.fields['faculty'].required = False
		self.fields['course'].required = False


class preliminaryRegistrationEvent(models.Model):
	surname = models.CharField(u'Фамилия', max_length=200)
	name = models.CharField(u'имя', max_length=200)
	thirdname = models.CharField(u'Отчество', max_length=200)
	email = models.CharField(u'Электронная почта', max_length=200)
	phone = models.CharField(u'Контактный телефон', max_length=200)
	university = models.CharField(u'Университет', max_length=200)
	faculty = models.CharField(u'Факультет', max_length=200, null = True)
	course = models.CharField(u'Курс', max_length=200, null = True)
	dateEntry = models.DateTimeField(auto_now=True)



# Create the form class.
class preliminaryRegistrationEventForm(ModelForm):
	class Meta:
		model = preliminaryRegistrationEvent
		exclude = ['dateEntry']
	def __init__(self, *args, **kwargs):
		# first call parent's constructor
		super(preliminaryRegistrationEventForm, self).__init__(*args, **kwargs)
		# there's a `fields` property now
		self.fields['faculty'].required = False
		self.fields['course'].required = False


