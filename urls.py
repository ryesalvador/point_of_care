from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('residents/', views.ResidentListView.as_view(), name='residents'),
    path('resident/<int:pk>', views.ResidentDetailView.as_view(), name='resident-detail'),
]
