from django.urls import path
from .views import CarListView, CarDetailView, SaleCreateView

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car_list'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('sale/<int:car_id>/', SaleCreateView.as_view, name='sale_create'),
    #path('category/<str:category>/', views.mashinki, name='car_list_by_category'),
]
