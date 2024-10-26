from django.urls import path
from .views import markets_view, single_market_view, sellers_view, product_view, single_product_view

urlpatterns = [
    path('market/', markets_view),
    path('market/<int:pk>/', single_market_view),
    path('seller/', sellers_view),
    path('product/', product_view),
    path('product/<int:pk>/', single_product_view),
]
    