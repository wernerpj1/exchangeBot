from rest_framework import serializers
from django.db.models import fields
from django.db import models
from .models import User
from exchange.serializers import AccountSerializer





class UserSerializer(serializers.ModelSerializer):
    account_user = AccountSerializer(many=True)
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'email',
            'account_user'
        )