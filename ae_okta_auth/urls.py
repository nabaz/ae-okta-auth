# -*- coding: utf-8 -*-
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name = 'ae_okta_auth'

urlpatterns = [
    path('acs/', views.acs),
    path('welcome/', views.welcome),
    path('denied/', views.denied),
]
