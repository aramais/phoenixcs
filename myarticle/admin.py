from django.contrib import admin
from myarticle.models import DefaultArticle, DefaultTag, TagEdge

admin.site.register(DefaultArticle)
admin.site.register(DefaultTag)
admin.site.register(TagEdge)