"""
URL configuration for todoList project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login),
    path('signup/',views.signup),
    path('additem/', views.add_item),
    path('updateitem/<int:pk>/', views.update_item,name='updateitem'),
path('showitem/', views.show_item),
    path('deleteitem/<int:pk>/',views.delete_item,name='deleteitem'),
path('logout/',views.logout),


]
