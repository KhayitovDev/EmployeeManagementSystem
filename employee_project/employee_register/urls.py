from django.urls import path
from . import views


urlpatterns=[
    path('', views.dash, name='dashboard'),
    path('create/', views.create, name='create'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete')

]