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

class UserInfoView(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    def list(self,request):
        return Response("nk")
# Create your views here.

class BitcoinPrice(viewsets.ModelViewSet):
    serializer_class = BitcoinInfoSerializer
    def list(self,request):
        # bitcoin_api_url = 'https://rest.coinapi.io/v1/exchangerate/BTC?apikey=19C1508E-76EA-4981-ADA6-9836945ADB63'
        bitcoin_api_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        response = requests.get(bitcoin_api_url)
        response_json = response.json()
        print(type(response_json))
        return Response(response_json)
    

