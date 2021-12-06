from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^main/', views.main_page, name='main-page'),

    #CREATE operation links
    url(r'^add-account/', views.add_account, name='main-page'),	
    url(r'^add-bank/', views.add_bank, name='main-page'),
    url(r'^add-user/', views.add_user, name='main-page'),

    #READ operation links
    url(r'^view-accounts/', views.view_accounts, name='view-accounts'),
]
