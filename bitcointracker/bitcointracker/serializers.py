from rest_framework import serializers
from bitcointracker.bitcointracker.models import UserInfo
from bitcointracker.bitcointracker.models import BitcoinInfo

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('username','email','age')

class BitcoinInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitcoinInfo
        fields = ('price','timestamp')