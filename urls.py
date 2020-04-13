from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('residents/', views.ResidentListView.as_view(), name='residents'),
    path('resident/<int:pk>', views.ResidentDetailView.as_view(), name='resident-detail'),
    path('resident/create/', views.ResidentCreate.as_view(), name='resident-create'),
    path('resident/<int:pk>/update/', views.ResidentUpdate.as_view(), name='resident-update'),
    path('resident/<int:pk>/delete/', views.ResidentDelete.as_view(), name='resident-delete'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
