from django.urls import path
from .views import markets_view, single_market_view, sellers_view, product_view, single_product_view, single_sellers_view, MarketsView

urlpatterns = [
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', single_market_view, name="market-detail"),
    path('seller/', sellers_view),
    path('seller/<int:pk>/', single_sellers_view),
    path('product/', product_view),
    path('product/<int:pk>/', single_product_view),
]
    