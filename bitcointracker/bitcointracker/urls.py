from django.urls import include, path
from rest_framework import routers

from bitcointracker.bitcointracker import views

router = routers.DefaultRouter()
router.register(r'users',views.UserInfoView)
router.register(r'bitcoinprice',views.BitcoinPrice,basename="price")
# router.register(r'bitcoinpricetracker',views.BitcoinPriceTracker,basename="tracker")


urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('tracker/',views.Bitcointracker)
]