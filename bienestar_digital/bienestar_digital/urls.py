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
from administration.views import administration_site
from django.contrib import admin
from django.urls import path
from home.views import login_view, signup, index, logout_view
from students.views import (
    student_data_view,
    asistence,
    registry_data_student,
    update_student,
)

urlpatterns = [
    path("administration/", administration_site.urls, name="admin"),
    path("", index, name="index"),
    path("accounts/signup/", signup, name="signup"),
    path("accounts/login/", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("students/asistence", asistence, name="mark_asistence"),
    path("students/my-data", student_data_view, name="student_data"),
    path("students/registry", registry_data_student, name="registry_student"),
    path("students/update", update_student, name='update_student'),
]
