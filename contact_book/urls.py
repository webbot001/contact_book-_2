"""
URL configuration for contact_book project.

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
from contact_app.views import *

urlpatterns = [
    path('', home),
    path('register/', register),
    path('del/<int:del_id>', remove),
    path('dashboard/', dashboard),
    path('logout/', logout),
    path('edit_pro/', edit_pro),
    path('add_cnt/', add_cnt),
    path('cnt/', cnt_show),
    path('update_contact/<int:upd_id>', update_contact),
    path('remove_contact/<int:del_id>', remove_contact),
    path('admin/', admin.site.urls),
]