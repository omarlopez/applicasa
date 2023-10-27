from rest_framework import serializers
from tools.models import Tools

class ToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tools
        exclude = []