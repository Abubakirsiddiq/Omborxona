from django.urls import path
from .views import *
from statsapp.views import StatsEdit

urlpatterns = [
    path('bolim/', BolimView.as_view(), name="bolim"),
    path('mahsulotlar/', MahsulotView.as_view(), name="mahsulotlar"),
    path('client/', ClientView.as_view(), name="client"),
    path('m_edit/<int:pk>/', MahsulotEdit.as_view(), name="m_edit"),
    path('c_edit/<int:pk>/', ClientEdit.as_view(), name="c_edit"),
]
