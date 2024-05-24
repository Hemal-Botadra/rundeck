from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),
    path('make/',views.make,name='make'),
    path('vote/<poll_id>',views.vote,name='vote'),
    path('results/<poll_id>',views.result,name='result'),
    ]