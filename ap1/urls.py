from django.contrib import admin
from django.urls import path
from .views import sinup,login,done
urlpatterns = [
    path('',sinup,name='sinup'),
    path('login',login,name='login'),
    path('done',done,name='done'),
]