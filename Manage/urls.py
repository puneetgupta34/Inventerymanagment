from django.urls import path

from . import views


urlpatterns = [
    path('', views.Manage, name='manage'),
    path('add_product', views.add_product, name='add_product'),
    path('add_location', views.add_location, name='add_location'),
    path('<int:Product_id>/edit_product',
         views.edit_product, name='edit_product'),
    path('<int:Location_id>/edit_location',
         views.edit_location, name='edit_location'),
    path('view_product', views.view_product, name='view_product'),
    path('view_location', views.view_location, name='view_location'),
    path('<int:Product_id>/productMovement',
         views.productMovement, name='productMovement'),





]
