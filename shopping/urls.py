"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from shop import views

urlpatterns = [
path('admin/', admin.site.urls),
path('', views.home, name='home'),
path(r'^home/$', views.home, name='home1'),
path ('items/',views.items, name='items'),
path ('stores/',views.stores, name='stores'),
path ('usages/',views.usages, name='usages'),
path('stores/<int:pk>/edit/', views.store_edit, name='store_edit'),
path('items/<int:pk>/edit/', views.item_edit, name='item_edit'),
path('usages/<int:pk>/edit/', views.usage_edit, name='usage_edit'),
url('login/',auth_views.LoginView.as_view(), name='login'),
path('accounts/', include('django.contrib.auth.urls')),
path('items/create/', views.item_new, name='item_new'),
path('stores/create/', views.store_new, name='store_new'),
path('usage/create/', views.usage_new, name='usage_new'),
]
