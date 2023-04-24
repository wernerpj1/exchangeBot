from rest_framework import serializers
from django.db.models import fields
from django.db import models
from .models import Exchange, Coin, Balance, Account, AccountMovement, Oportunity

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ( 
            'id',   
            'name',
            'max',
            'min'      
        )

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = (
            '__all__'
        )

class AccountMovimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountMovement
        fields = (
            'id',
            'entries',
            'outs',
            'date',
            'result'
        )

class AccountMovimentSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountMovement
        fields = (
            'balance',
            'entries',
            'outs'
        )

class BalanceSerializer(serializers.ModelSerializer):
    coin = CoinSerializer()
    account_moviment = AccountMovimentSerializer(many=True)
    
    class Meta:
        model = Balance
        fields = (
            'id', 
            'account_moviment',
            'coin'  
        )


class AccountSerializer(serializers.ModelSerializer):
    exchange = ExchangeSerializer(many=False)
    balance = BalanceSerializer(many=True)
    class Meta:
        model = Account
        fields = (
            'id',
            'exchange',
            'balance'
        )

class OportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Oportunity
        fields = (
            'exchangeBuy',
            'profit',
            'coin',
            'invest',
            'bidPrice',
            'bidQtity',
            'askPrice',
            'askQtity'
        )

class OportunityGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oportunity
        fields = (
            'date',
            'exchangeBuy',
            'profit',
            'coin',
            'invest',
            'bidPrice',
            'bidQtity',
            'askPrice',
            'askQtity'
        )


        
