from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from .botData import BotData, Oportunity
from .dollarToReal import DollarToReal
from .botDollar import OportunityDollar
from bot import views
from django.views.decorators.csrf import csrf_exempt
from .serializers import AccountMovimentSaveSerializer
import json
from bot.telegramBot import BotTelegram as tls
import config

# Create your views here.

def botDollarOportunity(request):
    telegramBot = tls(config.INSTA_KEY, config.CHAT_ID)
    oportunityBinance = OportunityDollar('mercado', 'binance')
    opportunityMercado = OportunityDollar('binance', 'mercado')
    dataBinance = oportunityBinance.oportunity()
    dataMercado = opportunityMercado.oportunity()
    if dataBinance['oportunity'] > dataMercado['oportunity'] and dataBinance['oportunity'] > 0.03:
        telegramBot.send_msg(str(dataBinance))
        return JsonResponse(dataBinance)
    if dataBinance['oportunity'] < dataMercado['oportunity'] and dataMercado['oportunity'] > 0.03:
        telegramBot.send_msg(str(dataMercado))
        return JsonResponse(dataMercado)

    return HttpResponse('Nada de bom na binance do dollar')

def botDollarOportunityMercado(request):
    telegramBot = tls(config.INSTA_KEY, config.CHAT_ID)
    oportunityMercado = OportunityDollar('binance', 'mercado')
    #opportunityMercado = OportunityDollar('binance', 'mercado')
    dataMercado = oportunityMercado.oportunity()
    """dataMercado = opportunityMercado.oportunity()
    if dataBinance['oportunity'] > dataMercado['oportunity'] and dataBinance['oportunity'] > 0.0045:
        telegramBot.send_msg(str(dataBinance))
        return JsonResponse(dataBinance)
    if dataBinance['oportunity'] < dataMercado['oportunity'] and dataMercado['oportunity'] > 0.0045:
        telegramBot.send_msg(str(dataMercado))
        return JsonResponse(dataMercado)"""
    if dataMercado['oportunity'] > 0.0045:
        telegramBot.send_msg(str(dataMercado))
        return JsonResponse(dataMercado)
    return HttpResponse('Nada de bom no mercado do dollar')


def botOportunity(request):
    telegramBot = tls(config.INSTA_KEY, config.CHAT_ID)
    oportunityBinance = Oportunity('mercado', 'binance')
    dataBinance = oportunityBinance.oportunity()
    oportunityMercado = Oportunity('binance', 'mercado')
    dataMercado = oportunityMercado.oportunity()
    if dataMercado['oportunity'] > dataBinance['oportunity'] and dataMercado['oportunity'] > 0.0045:
        #views.storeAccountMoviment()
        telegramBot.send_msg(str(dataMercado))
        return JsonResponse(dataMercado)
        
    if dataBinance['oportunity'] > dataMercado['oportunity'] and dataBinance['oportunity'] > 0.0045:
        telegramBot.send_msg(str(dataBinance))
        return JsonResponse(dataBinance)
    else:
        return HttpResponse("Nenhuma oportunidade boa")
    
    
@csrf_exempt
def storeAccountMoviment(request):
    if request.method == 'POST':
        response = AccountMovimentSaveSerializer(data=json.load(request), many=False)
        if response.is_valid():
            return HttpResponse('Account moviment saved with success')
        return HttpResponse(response.is_valid())
    
