from django.shortcuts import redirect, render

from product.models import Product

def product(request):
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
