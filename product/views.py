from django.shortcuts import redirect, render

from product.models import Product, User

def product(request):
    if request.session.get('username'):
        context = {}
        if request.method == 'GET':
          allproducts=Product.objects.all()
          context['product'] = allproducts 
          return render(request,'product.html',context=context)
        else:
              name = request.POST.get('name')
              description = request.POST.get('description')
              price = request.POST.get('price')
              category = request.POST.get('category')
              country = request.POST.get('country')
              image = request.FILES.get('image')
              create_date = request.POST.get('create_date')
              expire_date = request.POST.get('expire_date')
              Product.objects.create(name=name,
                description=description,
                price=price,
                category=category,
                country=country,
                image=image,
                create_date=create_date,
                expire_date=expire_date
                )
              allproducts=Product.objects.all()
              context['product'] = allproducts 
              return redirect('product')
    else:
      return redirect('login')

      
        
    
def delete_product(request,id):
     product=Product.objects.get(id=id)
     product.delete()
     return redirect('product')

def update_product(request,id):
    product=Product.objects.get(id=id)
    if request.method == 'GET':
        context = {}
        context['product'] = product 
        return render(request,'update.html',context=context)
    else:
          product.name = request.POST['name']
          product.description = request.POST['description']
          product.price = request.POST['price']
          product.category = request.POST['category']
          product.country = request.POST['country']
          product.image = request.FILES['image']
          product.create_date = request.POST['create_date']
          product.expire_date = request.POST['expire_date']
          product.save()
          return redirect('product')
    
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
  request.session.pop('username')
  return redirect('login.html')