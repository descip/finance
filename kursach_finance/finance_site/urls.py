from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),  # http://127.0.0.1:8000
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('about/', views.about.as_view(), name='about'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('edit/<int:pk>/', views.UpdatePage.as_view(), name='edit_page'),
    path('delete/<int:pk>/', views.DeletePage.as_view(), name='delete'),
]
