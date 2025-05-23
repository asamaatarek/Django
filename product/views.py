from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User as django_user
from .forms import CategoryForm, ProductForm
from django.views.decorators.http import require_http_methods
from product.models import Category, Product as ProductModel , User
class Product(View):
    def get(self,request):
        if request.session.get('username'):
          context = {}
          form = ProductForm()
          category_form = CategoryForm()
          allproducts=ProductModel.objects.all()
          categories = Category.objects.all() 
          context['product'] = allproducts
          context['categories'] = categories
          context['form'] = form
          context['category_form'] = category_form
          return render(request,'product.html',context=context)
        else:
          return redirect('login')
    def post(self,request):
        if request.session.get('username'):
          form = ProductForm(request.POST, request.FILES)
          category_form = CategoryForm(request.POST)
          if form.is_valid() and category_form.is_valid():
            product = form.save(commit=False)
            product.category = Category.objects.get(pk= category_form.cleaned_data['category'])
            print(category_form.cleaned_data['category'])
            product.save()
            return redirect('product')
        else:
          return redirect('login')
        
@require_http_methods(["GET", "POST" ])    
def delete_product(request,id):
      product = ProductModel.objects.filter(id=id).first()
      if product:
          product.delete()
      return redirect('product')

@require_http_methods(["GET", "POST"])   
def update_product(request,id):
   if request.session.get('username'):
      product=ProductModel.objects.filter(id=id).first()
      if not product:
            return redirect('product')
      if request.method == 'POST':
          form = ProductForm(request.POST, request.FILES, instance=product)
          category_form = CategoryForm(request.POST)
          if form.is_valid() and category_form.is_valid():
            product_update = form.save(commit=False)
            product_update.category = Category.objects.get(pk= category_form.cleaned_data['category'])
            product_update.save()
            return redirect('product')
      else:
          form = ProductForm(instance=product)
          category_form = CategoryForm(initial={'category': product.category.id})  
      context = {}
      category=Category.objects.all()
      context['product'] = product
      context['categories'] = category
      context['form'] = form
      context['category_form'] = category_form
      return render(request,'update.html',context=context)
   else:
      return redirect('login')


def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        user=User()
        user.username=request.POST['username']
        user.email=request.POST['email']
        user.password=request.POST['password']
        user.save()
        return redirect('login')
    
def login(request):
  if request.method == 'GET':
      return render(request,'login.html')
  else:
        user=User(username=request.POST['username'],password=request.POST['password'])
        if user:
            request.session['username'] = request.POST['username']
            return redirect('product')
        else:
            return render(request, 'login.html')
def logout(request):
  request.session.flush()
  return redirect('login')
 
          

   
            
              
        
  
         
""" def product(request):
    if request.session.get('username'):
        context = {}
        if request.method == 'GET':
          allproducts=Product.objects.all()
          categories = Category.objects.all()
          context['product'] = allproducts
          context['categories'] = categories
          return render(request,'product.html',context=context)
        else:
              name = request.POST.get('name')
              description = request.POST.get('description')
              price = request.POST.get('price')
              category_id = request.POST.get('category')
              category_instance = Category.objects.get(id=category_id)
              country = request.POST.get('country')
              image = request.FILES.get('image')
              create_date = request.POST.get('create_date')
              expire_date = request.POST.get('expire_date')
              Product.objects.create(name=name,
                description=description,
                price=price,
                category=category_instance,
                country=country,
                image=image,
                create_date=create_date,
                expire_date=expire_date
                )
              allproducts=Product.objects.all()
              categories = Category.objects.all()
              context['product'] = allproducts
              context['categories'] = categories
              return redirect('product')
    else:
      return redirect('login')

      
  
def update_product(request,id):
    product=Product.objects.get(id=id)
    if request.method == 'GET':
        context = {}
        category=Category.objects.all()
        context['product'] = product
        context['categories'] = category
        return render(request,'update.html',context=context)
    else:
          product.name = request.POST['name']
          product.description = request.POST['description']
          product.price = request.POST['price']
          category_id = request.POST['category']
          product.category = Category.objects.get(id=category_id)
          product.country = request.POST['country']
          product.image = request.FILES['image']
          product.create_date = request.POST['create_date']
          product.expire_date = request.POST['expire_date']
          product.save()
          return redirect('product')
 """   