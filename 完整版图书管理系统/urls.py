"""完整版图书管理系统 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^p_add', views.p_add),
    url(r'^p_delete', views.p_delete),
    url(r'^p_edit', views.p_edit),
    url(r'^p_select', views.p_select),
    url(r'^b_add', views.b_add),
    url(r'^b_delete', views.b_delete),
    url(r'^b_edit', views.b_edit),
    url(r'^b_select', views.b_select),
    url(r'^a_select', views.a_select),
    url(r'^a_add', views.a_add),
    url(r'^a_delete', views.a_delete),
    url(r'^a_edit', views.a_edit),

    url(r'^model',views.model),
    url(r'^edit',views.edit),
    url(r'^ajax_add',views.ajax_add),






    url(r'^b_myadd',views.b_myadd),
    url(r'^b_myedit',views.b_myedit),



    url('^student/(\w+).html$',views.student),
    url('^ck/(\w+).html?',views.ck),
    url('^ck1/(?P<a1>\w+).html',views.ck1),




]
