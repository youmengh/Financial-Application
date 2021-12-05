from django.contrib import admin
from .models import Customer, Bank, Accounts

# Register your models here.
admin.site.register(Customer)
admin.site.register(Bank)
admin.site.register(Accounts)