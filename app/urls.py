from django.urls import path
from app import views

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),   
    path('post/', views.FoodViews.as_view(), name='post'),
    path('post/<str:pk>/', views.FoodDetailViews.as_view(), name='post-detail'),
]
