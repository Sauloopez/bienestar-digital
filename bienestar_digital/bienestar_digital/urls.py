"""
URL configuration for bienestar_digital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home.views import login_view, signup, index, logout_view
from asistence.views import registry_student, asistence

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='index'),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/login/', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('asistence/', asistence, name='mark_asistence'),
    path('registryStudent', registry_student, name='registry_student')
]
