"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.http import HttpResponse, Http404
from django.urls import path
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Hello, gugu.</h1>")

def gugu(request):
    return render(request, "gugu.html")
def gugu1(request):
    return render(request, "gugu1.html")
def gugu2(request):
    return render(request, "gugu2.html")
def gugu3(request):
    return render(request, "gugu3.html")
def gugu4(request):
    return render(request, "gugu4.html")
def gugu5(request):
    return render(request, "gugu5.html")
def gugu6(request):
    return render(request, "gugu6.html")
def gugu7(request):
    return render(request, "gugu7.html")
def gugu8(request):
    return render(request, "gugu8.html")
def gugu9(request):
    return render(request, "gugu9.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('gugu/', gugu),
    path('gugu/gugu1/', gugu1),
    path('gugu/gugu2/', gugu2),
    path('gugu/gugu3/', gugu3),
    path('gugu/gugu4/', gugu4),
    path('gugu/gugu5/', gugu5),
    path('gugu/gugu6/', gugu6),
    path('gugu/gugu7/', gugu7),
    path('gugu/gugu8/', gugu8),
    path('gugu/gugu9/', gugu9),
]

