from django.urls import path
from .views import *

app_name = 'usermanagement'

urlpatterns = [
    path('', login, name='login'),
    path('dashboard', dashboard, name='dashboard'),
    path('validate', login_validate, name='login_validate'),
    path('logout/', logout, name='logout'),
]