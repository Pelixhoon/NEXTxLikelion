"""subjectProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from subjectApp import views
from subjectApp.views import AddMajorView, AddSubjectView, EditSubjectView, EditMajorView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addMajor', AddMajorView.as_view(), name="addMajor"),
    path('', views.home, name="home"),
    path('addSubject', AddSubjectView.as_view(), name="addSubject"),
    path('computer', views.computerSubjectView, name="computer"),
    path('economics', views.economicsSubjectView, name="economics"),
    path('editSubject/<int:pk>', EditSubjectView.as_view(), name="editSubject"),
    path('deleteSubject/<int:subject_pk>', views.DeleteSubjectView, name="deleteSubject"),
    path('editMajor/<int:pk>', EditMajorView.as_view(), name="editMajor"),
    path('deleteMajor/<int:major_pk>', views.DeleteMajorView, name="deleteMajor"),
]
