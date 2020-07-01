from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('process', views.process),
  path('create', views.create),
  path('delete', views.delete_dojo)
]