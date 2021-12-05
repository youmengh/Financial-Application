from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100, default="lastname")
    first_name = models.CharField(max_length=100, default="first")
    phone_number = models.CharField(max_length=100, default="phone")
    email = models.CharField(max_length=100, default="email")

    def __str__(self):
        return "Customer {}".format(self.last_name)

class Bank(models.Model):
    bank_name = models.CharField(max_length=100, default="bank")
    routing_number = models.IntegerField()
    bank_phone = models.CharField(max_length=100)

    def __str__(self):
        return "Bank {}".format(self.bank_name)
