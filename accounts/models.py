# encoding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')


class Profile_Experience(models.Model):
    profile = models.ForeignKey(MyProfile)
    company = models.CharField(max_length=200)
    jobstart = models.DateField()
    jobend = models.DateField()
    jobdescription = models.TextField()

class Project_Experience(models.Model):
    profile = models.ForeignKey(MyProfile)
    project = models.CharField(max_length=200)
    projectstart = models.DateField()
    projectend = models.DateField()
    projectdescription = models.TextField()

class Awards(models.Model):
    profile = models.ForeignKey(MyProfile)
    award = models.CharField(max_length=200)
