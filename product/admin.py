from django.contrib import admin

from product.models import Category, Product, User

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','image','create_date','expire_date','country','price','get_category')
    search_fields = ('name','description','image','create_date','expire_date','country','price','get_category')
    list_filter = ('name','description','image','create_date','expire_date','country','price','category')
    def get_category(self,obj):
        return [cat.name for cat in obj.category.all()]
    

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(User)