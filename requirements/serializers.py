from rest_framework import serializers
from requirements.models import Requirements, ItemRequirements

class ItemRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRequirements
        fields = ['created','description', 'isActive']

class RequirementsSerializer(serializers.ModelSerializer):
    main = ItemRequirementsSerializer(many=True, read_only=True)
    class Meta:
        model = Requirements
        fields = ['created', 'title', 'subtitle', 'isActive', 'main']

