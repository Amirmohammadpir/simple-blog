from django.contrib import admin
from .models import Article , Category
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('position','title', 'slug', 'status')
  list_filter = (['status'])
  search_fields = ('title', 'slug')
  prepopulated_field = {'slug': ('title',)}

  
admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'jpublished','category_to_str', 'status')
  list_filter = ('status','published')
  search_fields = ('title', 'description')
  prepopulated_field = {'slug': ('title',)}
  ordering = ['-status', '-published']

  def category_to_str(self, obj):
    return ", ".join([category.title for category in obj.category.all()])
    category_to_str.short_description = 'دسته بندی ها'
admin.site.register(Article, ArticleAdmin)