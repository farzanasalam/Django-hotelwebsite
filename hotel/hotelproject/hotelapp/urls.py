from django.contrib import admin
from django.urls import path
from . import views

app_name = "foodapp"

urlpatterns = [

    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('add/', views.add_food, name='add_food'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')

]
