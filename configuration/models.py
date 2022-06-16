from django.db import models
from usermanagement.models import *
# Create your models here.


class ReviewRating(models.Model):
    name = models.CharField(max_length=255, null=True)
    rating = models.IntegerField(null=True)
    shortlist = models.IntegerField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_rating_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_rating_updated_by')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'reviewrating'


class KPIConfig(models.Model):
    name = models.CharField(max_length=255)
    shortlist = models.IntegerField(null=True)
    year = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi_updated_by')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'kpiconfig'


class Supervisor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'supervisor'

class Project(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_updated_by')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'project'

class SBU(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi_sbu_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi_sbu_updated_by')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sub'


class SubSBU(models.Model):
    name = models.CharField(max_length=255)
    sub = models.ForeignKey(SBU, on_delete=models.CASCADE, related_name='SBU_by')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi_sub_sbu_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi_sub_sbu_updated_by')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sub_sub'


class KPIObjective(models.Model):
    name = models.CharField(max_length=255)
    shortlist = models.IntegerField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi_objective_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi_objective_updated_by')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'kpiobjective'


class Employee(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(null=True, blank=True)
    employee_id = models.CharField(max_length=255,unique=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    basic_salary = models.FloatField(default=None, null=True, blank=True)
    date_of_joining = models.DateField(null=True, blank=True)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, null=True, blank=True)
    sbu = models.ForeignKey(SBU, on_delete=models.CASCADE, null=True, blank=True)
    sub_sbu = models.ForeignKey(SubSBU, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee_updated_by')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employee'