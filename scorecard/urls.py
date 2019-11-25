from django.urls import path
from . import views

urlpatterns = [
    path('', views.scorecard_list, name='scorecard_list'),
    path('scorecard/<int:pk>/', views.scorecard_detail, name='scorecard_detail'),
    path('scorecard/new/', views.scorecard_list, name='new_card'),
]
