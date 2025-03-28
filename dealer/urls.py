from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from .views import CarListView, CarDetailView, SaleCreateView
from .views import register, login_view
from . import views
urlpatterns = [
    path('cars/', CarListView.as_view(), name='car_list'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('sale/<int:car_id>/', SaleCreateView.as_view, name='sale_create'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('About_us/', views.about, name='About_us'),
    #path('category/<str:category>/', views.mashinki, name='car_list_by_category'),
]
