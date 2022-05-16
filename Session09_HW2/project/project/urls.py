"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_page, name='list_page'),
    path('new', views.create_page, name='create_page'),
    path('detail/<int:post_pk>', views.detail_page, name='detail_page'),
    path('edit/<int:post_pk>', views.edit_page, name='edit_page'),
    path('delete/<int:post_pk>', views.delete, name='delete'),
    # 리스트에는 쉼표를 붙이는 습관
]
