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
    path('elements/', views.list_elements, name="list_elements"),
    path('elements/<str:slug>/', views.detail_element, name="detail_element"),
    path('elements/add', views.add_element, name="add_element"),
    path('elements/<str:slug>/save', views.save_element, name="save_element"),
    path('elements/<str:slug>/delete', views.delete_element, name="delete_element"),
    path('categories/<str:slug>/elements', views.list_elements_in_categorie, name="list_elements_in_categorie"),
    path('marques/<str:slug>/elements', views.list_elements_in_brand, name="list_elements_in_brand"),
]
