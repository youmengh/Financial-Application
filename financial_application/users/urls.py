from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^main/', views.main_page, name='main-page'),	
    url(r'^add-account/', views.add_account, name='main-page'),	
    url(r'^add-bank/', views.add_bank, name='main-page'),
    url(r'^add-user/', views.add_user, name='main-page')
]
