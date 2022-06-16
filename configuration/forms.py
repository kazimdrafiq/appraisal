from django.forms import ModelForm
from configuration.models import Employee, KPIConfig, ReviewRating, Supervisor, Project, SBU, SubSBU, KPIObjective
from django import forms


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = ['status','created_by','updated_by','updated_date']

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Name', 'required': 'required'}),
            "employee_id": forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Employee ID', 'required': 'required'}),
            "designation": forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Designation', 'required': 'required'}),
            "basic_salary": forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Salary', 'required': 'required'}),
            "date_of_joining": forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id':'html5-date-input'}),
            "sbu": forms.Select(attrs={'class': 'form-control'}),
            "sub_sbu": forms.Select(attrs={'class': 'form-control'}),
            "supervisor": forms.Select(attrs={'class': 'form-control'}),
            "project": forms.Select(attrs={'class': 'form-control'}),
        }

class KPIConfigForm(ModelForm):
    class Meta:
        model = KPIConfig
        exclude = ['created_by','updated_by','updated_date']

        widgets = {
            "shortlist": forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Shortlist', 'required': 'required'}),
            "name": forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Name', 'required': 'required'}),
            "year": forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Year', 'required': 'required'}),
        }

class ReviewRatingForm(ModelForm):
    class Meta:
        model = ReviewRating
        exclude = ['created_by', 'updated_by', 'updated_date']

        widgets = {
            "shortlist": forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Shortlist', 'required': 'required'}),
            "name": forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Name', 'required': 'required'}),
            "rating": forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Rating', 'required': 'required'}),
        }

class SupervisorForm(ModelForm):
    class Meta:
        model = Supervisor
        exclude = ['created_by', 'updated_by', 'updated_date']

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Name', 'required': 'required'}),
        }

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['created_by', 'updated_by', 'updated_date']

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Name', 'required': 'required'}),
        }

class SBUForm(ModelForm):
    class Meta:
        model = SBU
        exclude = ['created_by', 'updated_by', 'updated_date']

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Name', 'required': 'required'}),
        }

class SubSBUForm(ModelForm):
    class Meta:
        model = SubSBU
        exclude = ['created_by', 'updated_by', 'updated_date']

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Name', 'required': 'required'}),
            "sub": forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
        }

class KPIObjectiveForm(ModelForm):
    class Meta:
        model = KPIObjective
        exclude = ['created_by', 'updated_by', 'updated_date']

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Name', 'required': 'required'}),
            "shortlist": forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Shortlist', 'required': 'required'}),
        }