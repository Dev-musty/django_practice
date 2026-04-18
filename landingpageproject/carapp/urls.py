from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing-page'),
    # path('car', views.landing_page),
    path('add-car/', views.add_car, name='add-car'),
    path('cars/', views.car_list, name='car-list'),
    path('cars/<int:car_id>/delete/', views.delete_car, name='delete-car'),
]
