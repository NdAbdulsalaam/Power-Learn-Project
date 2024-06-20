from django.urls import path
from . import views

urlpatterns = [
    path('', views.pharmacy_list, name='pharmacy_list'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('pharmacy/<int:pharmacy_id>/', views.pharmacy_detail, name='pharmacy_detail'),
    path('pharmacy/<int:pharmacy_id>/add_review/', views.add_review, name='add_review'),
]