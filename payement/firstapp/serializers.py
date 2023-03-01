from rest_framework import serializers
from payment_api.models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    transaction_state = serializers.ReadOnlyField(default='Pending')
    payment_state = serializers.ReadOnlyField(default='Authorized')

    class Meta:
        model = Payment
        fields = ['sender', 'beneficiary', 'amount', 'payment_date', 'transaction_state', 'payment_state']
