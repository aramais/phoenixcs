from django.contrib import admin
from myarticle.models import Article, Tag, TagEdge, Category

from django import forms
from redactor.widgets import RedactorEditor

class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
           'text': RedactorEditor(),
        }

class TagEdgeInline(admin.StackedInline):
	model = TagEdge
	extra = 1

class ArticleAdmin(admin.ModelAdmin):
	inlines = [TagEdgeInline]
	form = ArticleAdminForm

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(TagEdge)
admin.site.register(Category)
