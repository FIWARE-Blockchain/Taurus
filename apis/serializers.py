from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Config


class ConfigSerializer(serializers.ModelSerializer):
    eventSpecification = serializers.JSONField()
    abi = serializers.JSONField()
    class Meta:
        model = Config
        fields = ['id', 'contractAddress', 'eventSpecification', 'abi', 'interval']