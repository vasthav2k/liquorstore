from django.contrib import admin
from .models import Category
from .models import Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name','manufactured_by']
    list_display_links=['id','name']
    search_fields=['name','description','manufactured_by']

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','is_published','category','price','is_sale','is_bestSeller']
    list_display_links=['id','name']
    search_fields=['name','description','category']
    list_filter=['category']
    list_editable=['is_published',]

    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)