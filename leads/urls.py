from django.urls import path
from . import views

app_name = 'leads'

urlpatterns = [
    path('add_lead/', views.add_lead, name='add_lead'),
    path('leads_list', views.leads_list, name='leads_list')
]