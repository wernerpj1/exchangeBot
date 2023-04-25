from django.shortcuts import render
from django.http import HttpResponse;
from django.http import JsonResponse
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
import json
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt



# Create your views here.


@api_view(['GET'])
def userData(request):
    user = User.objects.filter(id='1')
    user_serializer = UserSerializer(user, many=True)
    userAccounts = user_serializer.data
    context = {
        'user': user_serializer.data
    }
    return JsonResponse(context)
    #return Response(userAccounts)
    
@csrf_exempt
def storeUser(request):
    if request.method == 'POST':
        response = UserSerializer(data=json.load(request), many=False)
        if response.is_valid():
            response.save()
            return HttpResponse("User saved with success")
        return HttpResponse(response.is_valid())



    
