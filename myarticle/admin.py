from django.contrib import admin
from myarticle.models import DefaultArticle, DefaultTag, TagEdge, Category

from django import forms
from redactor.widgets import RedactorEditor

class DefaultArticleAdminForm(forms.ModelForm):
    class Meta:
        model = DefaultArticle
        widgets = {
           'text': RedactorEditor(),
        }

class TagEdgeInline(admin.StackedInline):
	model = TagEdge
	extra = 1

class ArticleAdmin(admin.ModelAdmin):
	inlines = [TagEdgeInline]
	form = DefaultArticleAdminForm

admin.site.register(DefaultArticle, ArticleAdmin)
admin.site.register(DefaultTag)
admin.site.register(TagEdge)
admin.site.register(Category)
