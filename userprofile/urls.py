from django.urls import path
from . import views


app_name = 'userprofile'

urlpatterns = [
    path('signup/', views.signup, name='signup')
]