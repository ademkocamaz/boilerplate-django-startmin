"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('index/', views.index, name='index'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/morris/', views.charts_morris, name='charts_morris'),
    path('tables/', views.tables, name='tables'),
    path('forms/', views.forms, name='forms'),
    path('ui/panels-wells/', views.ui_panels_wells, name='ui_panels-wells'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/notifications/', views.ui_notifications, name='ui_notifications'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),
    path('ui/icons/', views.ui_icons, name='ui_icons'),
    path('ui/grid/', views.ui_grid, name='ui_grid'),
    path('samples/blank/', views.samples_blank, name='samples_blank'),
    path('samples/login/', views.samples_login, name='samples_login'),



    path('admin/', admin.site.urls),
]
