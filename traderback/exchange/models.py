from django.db import models
from django.urls import reverse
from bot.models import User
import json
import decimal
from django.db.models import Sum, F, Func


# Create your models here.
        

class Coin(models.Model):
    name = models.CharField(max_length=255)
    max = models.DecimalField(decimal_places=10, max_digits=100, default=0)
    min = models.DecimalField(decimal_places=10, max_digits=100, default=0)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("coin_detail", kwargs={"pk": self.pk})
  
class Exchange(models.Model):
    exchange = models.CharField(max_length=255)
    tax = models.DecimalField(decimal_places=10, max_digits=10, default=0)
    
    def __str__(self):
        return self.exchange
    
    def get_absolute_url(self):
        return reverse("account_detail", kwargs={"pk": self.pk})

class Account(models.Model):
    user = models.ForeignKey(User,  related_name='account_user', on_delete=models.CASCADE)
    exchange = models.ForeignKey(Exchange, related_name='account', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.name+ '.'+ self.exchange.exchange

class Balance(models.Model):
    account = models.ForeignKey(Account, related_name='balance', on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, related_name='coin', on_delete=models.CASCADE)
    
    def __str__(self):
        return  str(self.id)+'.'+self.account.exchange.exchange+'.'+self.account.user.name+'.'+self.coin.name

class AccountMovement(models.Model):
    balance = models.ForeignKey(Balance, related_name='account_moviment', on_delete=models.CASCADE)
    entries = models.DecimalField(decimal_places=10, max_digits=1000, default=0)
    outs = models.DecimalField(decimal_places=10, max_digits=1000, default=0)
    date = models.DateTimeField(auto_now=True)
    
    @property
    def result(self):
        entry = AccountMovement.objects.filter(balance=self.balance).aggregate(entry=Sum('entries'))
        out = AccountMovement.objects.filter(balance=self.balance).aggregate(out=Sum('outs'))
        
        #resul = AccountMovement.objects.filter(balance=self.balance).aggregate(F('entry') - F('out'))
        balan = entry['entry'] - out['out']  
        
        return balan
    
    def get_absolute_url(self):
        """Retorna o URL para acessar uma instância específica do modelo."""
        return reverse('model-detail-view', args=[int(self.id)])

    def __str__(self):
        return str(self.pk)+'.'+self.balance.account.exchange.exchange+'.'+self.balance.account.user.name+'.'+self.balance.coin.name

class Oportunity(models.Model):
    exchangeBuy = models.CharField(max_length=255)
    profit = models.DecimalField(decimal_places=10, max_digits=1000, default=0)
    date = models.DateTimeField(auto_now=True)
    coin = models.CharField(max_length=255)
    invest = models.DecimalField(decimal_places=10, max_digits=1000, default=0) 
    bidPrice = models.DecimalField(decimal_places=10, max_digits=1000, default=0)
    bidQtity = models.DecimalField(decimal_places=10, max_digits=1000, default=0)
    askPrice = models.DecimalField(decimal_places=10, max_digits=1000, default=0)
    askQtity = models.DecimalField(decimal_places=10, max_digits=1000, default=0)
    
    def __str__(self):
        return str(self.date)
    
    def get_absolute_url(self):
        return reverse("oportunity_detail", kwargs={"pk": self.pk})