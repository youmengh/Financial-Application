from django.contrib import admin
from .models import Customer, Bank, Account, CardInfo, Transaction

# Register your models here.
admin.site.register(Customer)
admin.site.register(Bank)
admin.site.register(Account)
admin.site.register(CardInfo)
admin.site.register(Transaction)
