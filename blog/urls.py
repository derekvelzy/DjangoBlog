from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list') # for no relative path, go to the views.post_list view
]