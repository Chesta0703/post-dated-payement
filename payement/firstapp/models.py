from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    available_balance = models.DecimalField(max_digits=10, decimal_places=2)

class Payment(models.Model):
    sender = models.ForeignKey(Account, related_name='sender_payments', on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Account, related_name='beneficiary_payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    transaction_state = models.CharField(max_length=20, default='Pending')
    payment_state = models.CharField(max_length=20, default='Authorized')
