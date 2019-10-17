from django.contrib import admin
from .models import Product,Comment
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','author','created')
    list_display_links = ('title','author')
    prepopulated_fields = {"slug": ("title",)}

    
admin.site.register(Product,ProductAdmin)
admin.site.register(Comment)