from rest_framework import serializers
from mortgageadvisor.models import MortgageAdvisor, Brokers

class MortgageAdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MortgageAdvisor  
        exclude = []

class BrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brokers
        fields = ['created', 'broker', 'description', 'isActive']