from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_mixin_view), # Had to rewrite an underscore as mixin was not recognized at first
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/delete/', views.product_destroy_view),
    path('<int:pk>/', views.product_mixin_view),

]
