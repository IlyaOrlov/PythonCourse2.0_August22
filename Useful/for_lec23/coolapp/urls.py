from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('films/', views.films, name='films'),
    path('<int:film_id>/', views.new, name='new'),
]
