from django.urls import path
from .views import markets_view, single_market_view

urlpatterns = [
    path('', markets_view),
    path('<int:pk>', single_market_view),
]
    