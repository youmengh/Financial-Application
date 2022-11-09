from django.urls import re_path, include
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [

    re_path(r'^main/', views.main_page, name='main-page'),

    #CREATE operation links
    re_path(r'^add-account/', views.account_form, name='main-page'),
    re_path(r'^add-bank/', views.add_bank, name='main-page'),
    re_path(r'^add-user/', views.add_user, name='main-page'),
    re_path(r'^add-cardinfo/', views.add_cardinfo, name='main-page'),
    re_path(r'^add-transaction/', views.add_transaction, name='main-page'),
    re_path('account_update/<int:id>/', views.account_form, name='account_update'),
    re_path('account_delete/<int:id>/', views.account_delete, name='account_delete'),

    #READ operation links
    re_path(r'^view-accounts/', views.view_accounts, name='view-accounts'),
    re_path(r'^view-users/', views.view_users, name='view-users'),
    re_path(r'^view-banks/', views.view_banks, name='view-banks'),
    re_path(r'^view-cardinfo/', views.view_cardinfo, name='view-cardinfo'),
    re_path(r'^view-transactions/', views.view_transactions, name='view-transactions'),
]
