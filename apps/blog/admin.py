from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoryResource(resources.ModelResource):
  class Meta:
    model = Category

class CategoryAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
  search_fields = ['name']
  list_display = ('name', 'state', 'date_creation',)
  resource_class = CategoryResource

class AuthorResource(resources.ModelResource):
  class Meta:
    model = Author

class AuthorAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
  search_fields = ['names', 'surnames', 'mail']
  list_display = ('names', 'surnames', 'mail', 'state', 'date_creation',)
  resource_class = AuthorResource

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post)
