from django.urls import path
from . import views
from django.contrib.auth import views as v
from django.contrib.auth.views import redirect_to_login


app_name = 'userprofile'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', v.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', redirect_to_login, name='logout')
]