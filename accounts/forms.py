#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from userena.forms import EditProfileForm,SignupForm
from userena.utils import get_profile_model, get_user_model
try:
    from collections import OrderedDict
except ImportError:
    # Python 2.6 requires library
    from ordereddict import OrderedDict

class EditProfileFormExtra1(forms.ModelForm):
    """ Base form used for fields that are always required """
    first_name = forms.CharField(label=_(u'First name'),
                                 max_length=30,
                                 required=False)
    last_name = forms.CharField(label=_(u'Last name'),
                                 max_length=30,
                                 required=False)
    company = forms.CharField(label=_(u'Компания'),
                                 max_length=30,
                                 required=False)

    def __init__(self, *args, **kw):
        super(EditProfileFormExtra1, self).__init__(*args, **kw)
        # Put the first and last name at the top
        try:  # in Django < 1.7
            new_order = self.fields.keyOrder[:-2]
            new_order.insert(0, 'first_name')
            self.fields.keyOrder = new_order
        except AttributeError:  # in Django > 1.7
            new_order = [('first_name', self.fields['first_name']),
                         ('last_name', self.fields['last_name']),
                         ('company', self.fields['company']),
                         ]
            new_order.extend(list(self.fields.items())[:-2])
            self.fields = OrderedDict(new_order)

    class Meta:
        model = get_profile_model()
        exclude = ['user']

    def save(self, force_insert=False, force_update=False, commit=True):
        profile = super(EditProfileFormExtra1, self).save(commit=commit)
        # Save first and last name
        user = profile.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.company = self.cleaned_data['company']
        user.save()
        return profile
