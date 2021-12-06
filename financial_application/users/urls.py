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
    url(r'^view-users/', views.view_users, name='view-users'),
    url(r'^view-banks/', views.view_banks, name='view-banks'),
    url(r'^view-cardinfo/', views.view_cardinfo, name='view-cardinfo'),
    url(r'^view-transactions/', views.view_transactions, name='view-transactions'),
]
