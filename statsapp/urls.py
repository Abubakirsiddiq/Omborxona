from django.urls import path
from .views import *

urlpatterns = [
    path("", StatsView.as_view(), name="stats"),
    path('s_edit/<int:pk>/', StatsEdit.as_view(), name="s_edit"),
]
