from django.contrib import admin
from .models import Account, Coin, Exchange, Oportunity, Balance, AccountMovement

# Register your models here.
admin.site.register(AccountMovement)
admin.site.register(Account)
admin.site.register(Coin)
admin.site.register(Exchange)
admin.site.register(Oportunity)
admin.site.register(Balance)
