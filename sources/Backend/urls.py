"""
Project : Fonzy
File : urls
Author : DELEVACQ Wallerand
Date : 25/02/19
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
]