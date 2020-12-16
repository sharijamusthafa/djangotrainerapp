"""institute URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.shortcuts import render
from django.urls import path
from trainer.views import *

urlpatterns = [
    # path("",lambda request:render(request,"trainer/base.html")),
    path("reg",trainerRegistration,name="regg"),
    path("log",trainerLogin,name="logg"),
    path("hom",trainerHome,name="homm"),
    path("profile",createtrainerprofile,name="prof"),
   path("list",listProfile,name="list"),
    path("logout",logoutView,name="logout"),
    path("wel",welcome,name="wel"),
    path("delete/<int:pk>",deleteProfile,name="del"),
path("page",pageview,name="page"),
    path("apply",applyjob,name="apply"),
    path("listjob", listJob, name="joblist"),
    path("skill",skillview,name="skill")
]
