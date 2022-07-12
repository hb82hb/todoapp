"""Defines URL patterns for todoapps"""

from django.urls import path

from . import views

app_name = 'todoapps'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]
