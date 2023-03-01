from datetime import datetime
from payment_api.models import Payment
import time

def update_overdue_payments():
    overdue_payments = Payment.objects.filter(payment_date__lt=datetime.now(), transaction_state='Pending')
    for payment in overdue_payments:
        payment.transaction_state = 'Settled'
        payment.payment_state = 'Credited'
        payment.save()

        # update the sender's account balance
        sender = payment.sender
        sender.available_balance -= payment.amount
        sender.current_balance = sender.available_balance + Payment.objects.filter(sender=sender, transaction_state='Pending').aggregate(total_amount=models.Sum('amount'))['total_amount'] or 0
        sender.save()

        # update the beneficiary's account balance
        beneficiary = payment.beneficiary
        beneficiary.available_balance += payment.amount
        beneficiary.current_balance = beneficiary.available_balance + Payment.objects.filter(beneficiary=beneficiary, transaction_state='Pending').aggregate(total_amount=models.Sum('amount'))['total_amount'] or 0
        beneficiary.save()

while True:
    update_overdue_payments()
    time.sleep(1800)  # sleep for 30 minutes
