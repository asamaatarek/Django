from django import forms
from .models import Product,Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['category']
        widgets = {
            'description': forms.Textarea(attrs={'name':'body', 'rows':3, 'cols':30}),
            'create_date': forms.DateInput(attrs={'type': 'date'}),
            'expire_date': forms.DateInput(attrs={'type': 'date'}),
        }
class CategoryForm(forms.Form):
    category = forms.ChoiceField(choices=[ (category.pk,category.category) for category in Category.objects.all()])