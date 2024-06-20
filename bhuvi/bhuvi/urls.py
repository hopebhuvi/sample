"""
URL configuration for bhuvi project.

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
from bhuvi1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('h/',views.index),
    path('a/',views.index1),
    path('b/',views.index2),
    path('c/',views.index3),
    path('emp_reg/',views.emp_reg),
    path('e/',views.tech_add),
    path('empView/',views.empView),
    path('2/',views.setsession),
    path('3/',views.getsession),
    path('4/',views.delsession),
    path('5/',views.setcook),
    path('6/',views.getcook),
    path('stud_del/<int:o>',views.stud_del),
    path('stud_edit/<int:m>',views.stud_edit),
    path('stud_update/<int:b>',views.stud_update),
    # path('home/',views.form),
    path('',views.index1),
    path('login/',views.form),
    path('welcome/',views.edit),
    path('logout/',views.logout),
    path('edit/',views.n_edit),
    path('state/',views.stat),
    path('district/',views.dis)
]
