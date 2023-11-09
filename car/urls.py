from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("cars/", views.cars, name="cars"),
    path("cars/<int:id>", views.car_details, name="cars-details"),
    path('cars/update/<slug:pk>/', views.CarUpdate.as_view(), name='car_update'),
    path('cars/add/', views.CarCreate.as_view(), name='car_add'),
    path('mycar/', views.mycars, name='mycar'),
    path('cars/<int:id>/edit/', views.car_update, name='car_edit'),
    path('cars/<int:id>/createorder/', views.order_created, name='order_create'),
    path('detail/<int:id>/', views.order_detail, name='order_detail'),
    path('listorder/', views.order_list, name='order_list'),
    path('<int:id>/delete/', views.car_delete, name='car_delete'),
    path('listorder/<int:id>/deleteorder/', views.order_delete, name='order_delete'),
    path('contact/', views.contact, name='contact'),
    path('<int:id>/like/', views.like_update, name='like'),
    path('popularcar/', views.popular_car, name='popularcar'),
]
