from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('create', views.CreateIncident.as_view(), name='create'),
    path('all', views.IncidentList.as_view(), name='all'),
    path('user_all', views.IncidentListUser.as_view(), name='user_all'),
    path('details/<int:pk>', views.IncidentDetails.as_view(), name='details')
]
