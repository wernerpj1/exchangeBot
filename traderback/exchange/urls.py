from django.urls import path;

from . import views

urlpatterns = [
    path('bot-oportunity', views.botOportunity, name="bot-oportunity"),
    path('bot-dollar-oportunity', views.botDollarOportunity, name='bot-dollar-oportunity')
]