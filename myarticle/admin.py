from django.contrib import admin
from myarticle.models import DefaultArticle, DefaultTag, TagEdge, Category

class TagEdgeInline(admin.StackedInline):
	model = TagEdge
	extra = 1

class ArticleAdmin(admin.ModelAdmin):
	inlines = [TagEdgeInline]

admin.site.register(DefaultArticle, ArticleAdmin)
admin.site.register(DefaultTag)
admin.site.register(TagEdge)
admin.site.register(Category)