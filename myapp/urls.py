# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.edit, name='edit'),     # 追加
    path('delete/<int:pk>/', views.delete, name='delete'), # 追加
path('chart/', views.chart, name='chart'), # 追加
]
