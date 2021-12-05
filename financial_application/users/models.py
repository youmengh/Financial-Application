from django.db import models

class Customer(models.Model):
    last_name = models.CharField(max_length=100, default="lastname")
    first_name = models.CharField(max_length=100, default="first")
    phone_number = models.CharField(max_length=100, default="phone")
    email = models.CharField(max_length=100, default="email")

    def __str__(self):
        return "Customer {}".format(self.last_name)




