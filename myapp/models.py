from django.contrib.auth.hashers import make_password
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gen = models.CharField(max_length=10, null=True, blank=True)
    reg = models.CharField(max_length=10, null=True, blank=True)
    password = models.CharField(max_length=255)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return self.name

    def get_full_Person(self):
        """Returns the full address."""
        return f'{self.name}, {self.reg}'


class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.IntegerField(null=True)
    persons = models.ManyToManyField(Person)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.zipcode}"

    def get_full_address(self):
        """Returns the full address."""
        return f'{self.street}, {self.city}'

    class Meta:
        db_table = 'addresss'


class Account(models.Model):
    account_type = models.CharField(max_length=20, null=True, blank=True)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ifsc_code = models.CharField(max_length=20, unique=True)
    branch = models.CharField(max_length=20)
    persons = models.ManyToManyField(Person)

    def __str__(self):
        return f"{self.account_number}"
