from django.urls import path
from .views import *

app_name = 'configuration'

urlpatterns = [

    # employee
    path('epm/', EmployeeListView.as_view(), name='EmployeeListView'),
    path('add/', EmployeeCreateView.as_view(), name='EmployeeCreateView'),
    path('employeeedit/edit/<pk>/', EmployeeUpdateView.as_view(), name='EmployeeUpdateView'),
    path('employeeedit/delete/<pk>/', EmployeeDeleteView.as_view(), name='EmployeeDeleteView'),

    # kpi-configuration
    path('kpiconfig/', KPIConfigListView.as_view(), name='KPIConfigListView'),
    path('kpiconfigadd/', KPIConfigCreateView.as_view(), name='KPIConfigCreateView'),
    path('kpiconfigedit/edit/<pk>/', KPIConfigUpdateView.as_view(), name='KPIConfigUpdateView'),
    path('kpiconfigdelete/delete/<pk>/', KPIConfigDeleteView.as_view(), name='KPIConfigDeleteView'),

    # review-rating
    path('reviewrating/', ReviewRatingListView.as_view(), name='ReviewRatingListView'),
    path('reviewratingadd/', ReviewRatingCreateView.as_view(), name='ReviewRatingCreateView'),
    path('reviewratingedit/edit/<pk>/', ReviewRatingUpdateView.as_view(), name='ReviewRatingUpdateView'),
    path('reviewratingdeleteView/delete/<pk>/', ReviewRatingDeleteView.as_view(), name='ReviewRatingDeleteView'),

    # supervisor
    path('supervisor/', SupervisorListView.as_view(), name='SupervisorListView'),
    path('supervisoradd/', SupervisorCreateView.as_view(), name='SupervisorCreateView'),
    path('supervisoredit/edit/<pk>/', SupervisorUpdateView.as_view(), name='SupervisorUpdateView'),
    path('supervisoredelete/delete/<pk>/', SupervisorDeleteView.as_view(), name='SupervisorDeleteView'),

    # project
    path('project/', ProjectListView.as_view(), name='ProjectListView'),
    path('projectadd/', ProjectCreateView.as_view(), name='ProjectCreateView'),
    path('projectedit/edit/<pk>/', ProjectUpdateView.as_view(), name='ProjectUpdateView'),
    path('projectdelete/delete/<pk>/', ProjectDeleteView.as_view(), name='ProjectDeleteView'),

    # sbu
    path('sbu/', SBUListView.as_view(), name='SBUListView'),
    path('sbuadd/', SBUCreateView.as_view(), name='SBUCreateView'),
    path('sbuedit/edit/<pk>/', SBUUpdateView.as_view(), name='SBUUpdateView'),
    path('sbudelete/delete/<pk>/', SBUDeleteView.as_view(), name='SBUDeleteView'),

    # sub-sbu
    path('subsbu/', SubSBUListView.as_view(), name='SubSBUListView'),
    path('subsbuadd/', SubSBUCreateView.as_view(), name='SubSBUCreateView'),
    path('subsbuedit/edit/<pk>/', SubSBUUpdateView.as_view(), name='SubSBUUpdateView'),
    path('subsbudelete/delete/<pk>/', SubSBUDeleteView.as_view(), name='SubSBUDeleteView'),

    # kpi-objective
    path('kpiobjective/', KPIObjectiveListView.as_view(), name='KPIObjectiveListView'),
    path('kpiobjectivebuadd/', KPIObjectiveCreateView.as_view(), name='KPIObjectiveCreateView'),
    path('kpiobjectiveedit/edit/<pk>/', KPIObjectiveUpdateView.as_view(), name='KPIObjectiveUpdateView'),
    path('kpiobjectivedelete/delete/<pk>/', KPIObjectiveDeleteView.as_view(), name='KPIObjectiveDeleteView'),
]