from django.contrib import admin

from product.models import Category, Product, User

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','image','create_date','expire_date','country','price','get_category')
    search_fields = ('name','description','create_date','expire_date','country','price','category__category')
    list_filter = ('name','description','image','create_date','expire_date','country','price','category')
    # Forign key 
    def get_category(self,obj):
        return obj.category.category # here we return one category
    # M to M
    """ def get_category(self,obj):
        return [cat.name for cat in obj.category.all()] #bc we return multiple categories""" 
    

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(User)