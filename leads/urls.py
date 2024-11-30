from django.urls import path
from . import views

app_name = 'leads'

urlpatterns = [
    path('add_lead/', views.add_lead, name='add_lead'),
    path('leads_list/', views.leads_list, name='leads_list'),
    path('<int:pk>/', views.leads_details, name='leads_details'),
    path('<int:pk>/delete/', views.delete_leads, name='delete_leads'),
    path('<int:pk>/edit/', views.edit_leads, name='edit_leads'),
    path('<int:pk>/convert/', views.converted_to_client, name='leads_convert'),
]