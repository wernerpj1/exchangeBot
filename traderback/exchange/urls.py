from django.urls import path;

from . import views

urlpatterns = [
    path('bot-oportunity', views.botOportunity, name="bot-oportunity"),
    path('bot-dollar-oportunity', views.botDollarOportunity, name='bot-dollar-oportunity'),
    path('store_account_moviment', views.storeAccountMoviment, name='store_account_moviment'),
    path('bot-dollar-mercado-oportunity', views.botDollarOportunityMercado, name='bot-dollar-mercado-oportunity')
    
]