from django.urls import path
from .views import *

urlpatterns = [
    path("kpi_form_demo/",kpi_form_demo,name='kpi_form_demo'),
    path("kpi_form/",kpi_form,name='kpi_form'),
]