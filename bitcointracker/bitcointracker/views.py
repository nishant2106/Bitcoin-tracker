from tracemalloc import Snapshot
from django.shortcuts import render
from rest_framework import viewsets
from bitcointracker import bitcointracker
from bitcointracker.bitcointracker import serializers

from bitcointracker.bitcointracker.models import UserInfo
from bitcointracker.bitcointracker.serializers import UserInfoSerializer

from bitcointracker.bitcointracker.models import BitcoinInfo
from bitcointracker.bitcointracker.serializers import BitcoinInfoSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import django_tables2 as tables

class UserInfoView(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
# Create your views here.

class BitcoinPrice(viewsets.ModelViewSet):
    queryset = BitcoinInfo.objects.all()
    serializer_class = BitcoinInfoSerializer
    def list(self,request):
        bitcoin_api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        response = requests.get(bitcoin_api_url)
        response_json = response.json()
        p = BitcoinInfo(price = response_json["bpi"]["USD"]["rate"], timestamp =response_json["time"]["updated"])
        p.save()
        return Response({response_json["bpi"]["USD"]["rate"],response_json["time"]["updated"]})

# this class will create the table just like how we create forms
class SimpleTable(tables.Table):
   class Meta:
      model = BitcoinInfo


@api_view(['GET'])
def Bitcointracker(request):
    queryset = SimpleTable(BitcoinInfo.objects.all())
    queryset.paginate(page=request.GET.get("page", 1), per_page=10)
    return render(request,'templates/table_example.html',locals())


    

