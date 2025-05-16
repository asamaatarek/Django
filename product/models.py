from django.db import models

cat_product=[(('fruits'),('fruits')),(('vegtables'),('vegtables')),(('Dairy'),('Dairy')),(('baked goods'),('baked goods'))]

class Category(models.Model):
    category=models.CharField(max_length=50,choices=cat_product)
    def __str__(self):
        return self.category
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=70,null=True)
    image=models.FileField(upload_to='productImages/',null=False, blank=False)
    create_date=models.DateField()
    expire_date=models.DateField()
    country= models.CharField(max_length=50)
    price= models.DecimalField(max_digits=6, decimal_places=2)
    category=models.ManyToManyField(Category)

    def __str__(self):
        return str(self.id)
class User(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)
    email=models.EmailField(unique=True)