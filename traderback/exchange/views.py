from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from .botData import BotData, Oportunity
from .dollarToReal import DollarToReal
from .botDollar import OportunityDollar

# Create your views here.

def botDollarOportunity(request):
    oportunity = OportunityDollar('mercado', 'binance')
    #coin = [2500.00, 50.00]
    #changeCoin = DollarToReal(coin)
    #changeCoin = changeCoin.convert()

    return JsonResponse(oportunity.oportunity())

def botOportunity(request):

    oportunityBinance = Oportunity('mercado', 'binance')
    dataBinance = oportunityBinance.oportunity()
    oportunityMercado = Oportunity('binance', 'mercado')
    dataMercado = oportunityMercado.oportunity()
    if dataMercado['oportunity'] > dataBinance['oportunity'] and dataMercado['oportunity'] > 0.0045:
        return JsonResponse(dataMercado)
    if dataBinance['oportunity'] > dataMercado['oportunity'] and dataBinance['oportunity'] > 0.0045:
        return JsonResponse(dataBinance)
    else:
        return 