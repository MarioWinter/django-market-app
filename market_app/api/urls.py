from django.urls import path, include
from .views import markets_view, single_market_view, sellers_view, product_view, single_product_view, single_sellers_view, MarketsView, MarketDetailView, ProductViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketDetailView.as_view(), name="market-detail"),
    path('seller/', sellers_view),
    path('seller/<int:pk>/', single_sellers_view),
    # path('product/', product_view),
    # path('product/<int:pk>/', single_product_view),
]
    