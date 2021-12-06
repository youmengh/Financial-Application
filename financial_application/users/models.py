from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100, default="lastname")
    first_name = models.CharField(max_length=100, default="first")
    phone_number = models.CharField(max_length=100, default="phone")
    email = models.CharField(max_length=100, default="email")

    def __str__(self):
        return "{}".format(self.last_name)

class Bank(models.Model):
    bank_name = models.CharField(max_length=100, default="bank")
    routing_number = models.BigIntegerField()
    bank_phone = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.bank_name)

class Account(models.Model):
    account_num = models.BigIntegerField()
    account_name = models.CharField(max_length=100, default="My Account")
    account_type = models.CharField(max_length=100, default="Checking")
    account_bal = models.FloatField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bank_name = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def __str__(self):
        return"Account: {}".format(self.account_num)

class CardInfo(models.Model):
    card_number = models.BigIntegerField()
    card_holder = models.CharField(max_length=100, default="holder")
    card_issuer = models.CharField(max_length=100, default="issuer")
    security_code = models.CharField(max_length=3, default="000")
    expiration = models.CharField(max_length=100, default="MM/YY")
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    last_four_digits = models.IntegerField(primary_key=True)

    def __str__(self):
        return"****-****-****-{}".format(self.last_four_digits)

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_num = models.ForeignKey(Account, on_delete=models.CASCADE)
    previous_balance = models.FloatField()
    amount_paid = models.FloatField()
    new_balance = models.FloatField()
    last_four_digits = models.ForeignKey(CardInfo, on_delete=models.CASCADE)

    def __str__(self):
        return("Transaction: {}".format(self.transaction_id))
