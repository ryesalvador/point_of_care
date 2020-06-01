from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('residents/', views.ResidentListView.as_view(), name='residents'),
    path('resident/<int:pk>', views.ResidentDetailView.as_view(), name='resident-detail'),
    path('resident/create/', views.ResidentCreate.as_view(), name='resident-create'),
    path('resident/<int:pk>/update/', views.ResidentUpdate.as_view(), name='resident-update'),
    path('resident/<int:pk>/delete/', views.ResidentDelete.as_view(), name='resident-delete'),
    path('interventions/', views.InterventionListView.as_view(), name='interventions'),
    path('intervention/<int:pk>', views.InterventionDetailView.as_view(), name='intervention-detail'),
    path('intervention/create/', views.InterventionCreate.as_view(), name='intervention-create'),
    path('intervention/<int:pk>/update/', views.InterventionUpdate.as_view(), name='intervention-update'),
    path('intervention/<int:pk>/delete/', views.InterventionDelete.as_view(), name='intervention-delete'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
