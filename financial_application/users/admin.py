from django.contrib import admin
from .models import Customer, Bank, Account, CardInfo

# Register your models here.
admin.site.register(Customer)
admin.site.register(Bank)
admin.site.register(Account)
admin.site.register(CardInfo)