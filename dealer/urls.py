from django.urls import path
from .views import CarListView, CarDetailView, SaleCreateView
from .views import register, login_view

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car_list'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('sale/<int:car_id>/', SaleCreateView.as_view, name='sale_create'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    #path('category/<str:category>/', views.mashinki, name='car_list_by_category'),
]
