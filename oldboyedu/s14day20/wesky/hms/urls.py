"""wesky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from hms import views

urlpatterns = [
    url(r'^business/', views.Business.as_view()),
    url(r'^host/', views.Host.as_view(), name="host"),
    url(r'^backdoor/', views.Backdoor.as_view()),
    url(r'^door/', views.Door.as_view()),
    url(r'^del/', views.Del.as_view()),
    url(r'^app/', views.App.as_view()),
    url(r'^del_rhost/', views.Delrhost.as_view()),
    url(r'^edit/', views.Edit.as_view()),
]
