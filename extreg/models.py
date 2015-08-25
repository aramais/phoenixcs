# coding:utf-8
from django.db import models
from django.forms import ModelForm

# Create your models here.

studyForms = [('bach', 'Бакалавриат'), 
	('spec', 'Специалитет'), 
	('mag', 'Магистратура'), 
	('other', 'Другое')]

years = [(str(year), str(year)) for year in range(2000,2025)] + [('other', 'Другое')]




class preliminaryRegistration(models.Model):
	surname = models.CharField(u'Фамилия', max_length=200)
	name = models.CharField(u'имя', max_length=200)
	thirdname = models.CharField(u'Отчество', max_length=200)
	email = models.EmailField(u'Электронная почта')
	phone = models.CharField(u'Контактный телефон', max_length=200)
	university = models.CharField(u'ВУЗ', max_length=200)
	faculty = models.CharField(u'Факультет', max_length=200, null = True)
	studyForm = models.CharField(u'Степень', max_length=200, null = True, choices = studyForms, default = 'bach')
	yearEnd = models.CharField(u'Год окончания', max_length=200, null = True, choices = years, default = '2017')
	dateEntry = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.name + " " + self.surname



# Create the form class.
class preliminaryRegistrationForm(ModelForm):
	class Meta:
		model = preliminaryRegistration
		exclude = ['dateEntry']
	def __init__(self, *args, **kwargs):
		# first call parent's constructor
		super(preliminaryRegistrationForm, self).__init__(*args, **kwargs)
		# there's a `fields` property now
		#self.fields['faculty'].required = False
		#self.fields['course'].required = False



