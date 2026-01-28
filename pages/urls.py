# pages/urls.py
from django.urls import path
from .views import home, sobre, contato, ajuda

urlpatterns = [
    path('', home, name='home'),
    path("sobre/", sobre, name='sobre'),
    path('contato/', contato, name='contato'),
    path('ajuda/', ajuda, name='ajuda')
]
