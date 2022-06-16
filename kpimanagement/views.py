from multiprocessing import context
from django.shortcuts import render
from datetime import date
# Create your views here.
todays_date = date.today()

def kpi_form_demo(request):
    context = {

    }
    return render(request,'configuration/KPI/KPI-Sample.html',context)

def kpi_form(request):
    
    context = {
        "year" : todays_date.year,
    }
    return render(request,'configuration/KPI/KPI_FORM.html',context)