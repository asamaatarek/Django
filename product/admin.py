from django.contrib import admin

from product.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','image','create_date','expire_date','country','price','category')
    search_fields = ('name','description','image','create_date','expire_date','country','price','category')
    list_filter = ('name','description','image','create_date','expire_date','country','price','category')
admin.site.register(Product,ProductAdmin)