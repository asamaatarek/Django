"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from school.views import home,contact,welcome
from product.views import product,delete_product,update_product,login,signup
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('welcome/', welcome, name='welcome'),
    path('product/', product, name='product'),
    path('delete_product/<int:id>', delete_product, name='delete_product'),
    path('update_product/<int:id>', update_product, name='update_product'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
