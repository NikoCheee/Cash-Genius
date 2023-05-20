from django.contrib import admin
from .models import Article, EnglishArticle, Category, Tag


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ArticleAdmin(admin.ModelAdmin):
    exclude = ('author', )


admin.site.register(Article, ArticleAdmin)
admin.site.register(EnglishArticle)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
