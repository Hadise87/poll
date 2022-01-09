from django.urls import path 

from . import views
# from pollster import polls
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'), 
]
