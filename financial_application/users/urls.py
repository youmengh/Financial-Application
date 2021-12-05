from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    #create bot
    url(r'^main/', views.main_page, name='main-page'),	
    url(r'^add-account/', views.add_account, name='main-page'),	
    url(r'^add-bank/', views.add_bank, name='main-page'),
    #listing bots

]
