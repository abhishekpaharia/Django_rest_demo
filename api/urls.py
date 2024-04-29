
from django.urls import path
from . import views

urlpatterns = [
    path('drinks/', views.drink_list),
    path('drinks/<str:pk>', views.drink_detail)
]