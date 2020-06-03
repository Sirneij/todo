from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListAPIView.as_view()),
    path('<int:pk>/', views.TodoDetailsAPIView.as_view()),
]
