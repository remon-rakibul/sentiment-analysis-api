from django.urls import path
from . import views

urlpatterns = [
    path('health', views.Health_check.as_view(), name='health'),
    path('analyze', views.PredictSentimentView.as_view(), name='prediction'),
]