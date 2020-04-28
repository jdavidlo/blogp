from django.urls import path
from . import views

urlpatterns = [
    path('', views.datos_list, name='datos_list'),
    path('post/<int:pk>/', views.datos_detail, name='datos_detail'),
    path('post/new', views.datos_new, name='datos_new'),
     path('post/<int:pk>/edit/', views.datos_edit, name='datos_edit'),
]