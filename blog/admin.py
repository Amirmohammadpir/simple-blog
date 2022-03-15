from django.contrib import admin
from .models import Article 
class ArticleAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'jpublished', 'status')
  list_filter = ('status','published')
  search_fields = ('title', 'description')
  prepopulated_field = {'slug': ('title',)}
  ordering = ['-status', '-published']
admin.site.register(Article, ArticleAdmin)
