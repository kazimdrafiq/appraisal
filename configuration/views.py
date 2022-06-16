from datetime import datetime
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import requests
from configuration.forms import EmployeeForm, KPIConfigForm, ReviewRatingForm, SupervisorForm, ProjectForm, SBUForm, SubSBUForm, KPIObjectiveForm
from configuration.models import *
from django.utils.decorators import method_decorator
from usermanagement.decorators import login_required, access_permission_required
# Create your views here.
# @method_decorator(login_required("logged_in", 'usermanagement:login'), name='dispatch')
# @method_decorator(access_permission_required, name='dispatch')


class EmployeeListView(ListView):
    model = Employee
    template_name = 'configuration/employee/employee_list.html'
    context_object_name = 'employee'

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        context['data'] = userdata
        context['employee'] = self.model.objects.all()
        return context

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'configuration/employee/employee_add.html'
    success_url = reverse_lazy('configuration:EmployeeListView')

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(EmployeeCreateView, self).get_context_data(**kwargs)
        context['data'] = userdata
        context['form'] = self.form_class
        return context

    def form_valid(self, form):
        print(form)
        if form.is_valid:
            employee = form.save(commit=False)
            employee.created_date = datetime.now()
            employee.updated_date = datetime.now()
            employee.created_by_id =self.request.session['id']
            employee.updated_by_id =self.request.session['id']
            employee.save()
            messages.success(self.request, 'Data Successfully Saved')
            return super(EmployeeCreateView, self).form_valid(form)
        else:
            messages.error(self.request, 'invalid')
            return super(EmployeeCreateView, self).form_invalid(form)

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'configuration/employee/employee_update.html'
    success_url = reverse_lazy('configuration:EmployeeListView')
    context_object_name = 'employeeedit'

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        context['data'] = userdata
        # context['form'] = self.form_class
        return context

    def form_valid(self, form):

        if form.is_valid:
            employee = form.save(commit=False)
            employee.updated_by_id =self.request.session['id']
            employee.updated_date = datetime.now()
            employee.save()
            messages.success(self.request, 'Data Successfully Updated')
            return super(EmployeeUpdateView, self).form_valid(form)
        else:
            messages.error(self.request, 'invalid')
            return super(EmployeeUpdateView, self).form_invalid(form)

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'configuration/employee/employee_delete.html'
    success_url = reverse_lazy('configuration:EmployeeListView')

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(EmployeeDeleteView, self).get_context_data(**kwargs)
        context['data'] = userdata
        return context

    def get_success_url(self):
        messages.success(self.request, 'Data Successfully Deleted')
        return reverse_lazy('configuration:EmployeeListView')



class KPIConfigListView(ListView):
    model = KPIConfig
    template_name = 'configuration/kpiconfiguration/kpiconfiguration_list.html'
    context_object_name = 'kpiconfigs'

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(KPIConfigListView, self).get_context_data(**kwargs)
        context['data'] = userdata
        context['employee'] = self.model.objects.all()
        return context

class KPIConfigCreateView(CreateView):
    model = KPIConfig
    form_class = KPIConfigForm
    template_name = 'configuration/kpiconfiguration/kpiconfiguration_add.html'
    success_url = reverse_lazy('configuration:KPIConfigListView')

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(KPIConfigCreateView, self).get_context_data(**kwargs)
        context['data'] = userdata
        context['form'] = self.form_class
        return context

    def form_valid(self, form):
        print(form)
        if form.is_valid:
            kpiconfig = form.save(commit=False)
            kpiconfig.created_date = datetime.now()
            kpiconfig.updated_date = datetime.now()
            kpiconfig.created_by_id =self.request.session['id']
            kpiconfig.updated_by_id =self.request.session['id']
            kpiconfig.save()
            messages.success(self.request, 'Data Successfully Saved')
            return super(KPIConfigCreateView, self).form_valid(form)
        else:
            messages.error(self.request, 'invalid')
            return super(KPIConfigCreateView, self).form_invalid(form)

class KPIConfigUpdateView(UpdateView):
    model = KPIConfig
    form_class = KPIConfigForm
    template_name = 'configuration/kpiconfiguration/kpiconfiguration_update.html'
    success_url = reverse_lazy('configuration:KPIConfigListView')
    context_object_name = 'kpiconfigedit'

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(KPIConfigUpdateView, self).get_context_data(**kwargs)
        context['data'] = userdata
        # context['form'] = self.form_class
        return context

    def form_valid(self, form):

        if form.is_valid:
            kpiconfig = form.save(commit=False)
            kpiconfig.updated_by_id =self.request.session['id']
            kpiconfig.updated_date = datetime.now()
            kpiconfig.save()
            messages.success(self.request, 'Data Successfully Updated')
            return super(KPIConfigUpdateView, self).form_valid(form)
        else:
            messages.error(self.request, 'invalid')
            return super(KPIConfigUpdateView, self).form_invalid(form)

class KPIConfigDeleteView(DeleteView):
    model = KPIConfig
    template_name = 'configuration/kpiconfiguration/kpiconfiguration_delete.html'
    success_url = reverse_lazy('configuration:KPIConfigListView')

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(KPIConfigDeleteView, self).get_context_data(**kwargs)
        context['data'] = userdata
        return context

    def get_success_url(self):
        messages.success(self.request, 'Data Successfully Deleted')
        return reverse_lazy('configuration:KPIConfigListView')



class ReviewRatingListView(ListView):
    model = ReviewRating
    template_name = 'configuration/reviewrating/reviewrating_list.html'
    context_object_name = 'reviewratings'

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(ReviewRatingListView, self).get_context_data(**kwargs)
        context['data'] = userdata
        context['employee'] = self.model.objects.all()
        return context

class ReviewRatingCreateView(CreateView):
    model = ReviewRating
    form_class = ReviewRatingForm
    template_name = 'configuration/reviewrating/reviewrating_add.html'
    success_url = reverse_lazy('configuration:ReviewRatingListView')

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(ReviewRatingCreateView, self).get_context_data(**kwargs)
        context['data'] = userdata
        context['form'] = self.form_class
        return context

    def form_valid(self, form):
        print(form)
        if form.is_valid:
            reviewrating = form.save(commit=False)
            reviewrating.created_date = datetime.now()
            reviewrating.updated_date = datetime.now()
            reviewrating.created_by_id =self.request.session['id']
            reviewrating.updated_by_id =self.request.session['id']
            reviewrating.save()
            messages.success(self.request, 'Data Successfully Saved')
            return super(ReviewRatingCreateView, self).form_valid(form)
        else:
            messages.error(self.request, 'invalid')
            return super(ReviewRatingCreateView, self).form_invalid(form)

class ReviewRatingUpdateView(UpdateView):
    model = ReviewRating
    form_class = ReviewRatingForm
    template_name = 'configuration/reviewrating/reviewrating_update.html'
    success_url = reverse_lazy('configuration:ReviewRatingListView')
    context_object_name = 'reviewratings'

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(ReviewRatingUpdateView, self).get_context_data(**kwargs)
        context['data'] = userdata
        # context['form'] = self.form_class
        return context

    def form_valid(self, form):

        if form.is_valid:
            reviewrating = form.save(commit=False)
            reviewrating.updated_by_id =self.request.session['id']
            reviewrating.updated_date = datetime.now()
            reviewrating.save()
            messages.success(self.request, 'Data Successfully Updated')
            return super(ReviewRatingUpdateView, self).form_valid(form)
        else:
            messages.error(self.request, 'invalid')
            return super(ReviewRatingUpdateView, self).form_invalid(form)

class ReviewRatingDeleteView(DeleteView):
    model = ReviewRating
    template_name = 'configuration/reviewrating/reviewrating_delete.html'
    success_url = reverse_lazy('configuration:ReviewRatingListView')

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(ReviewRatingDeleteView, self).get_context_data(**kwargs)
        context['data'] = userdata
        return context

    def get_success_url(self):
        messages.success(self.request, 'Data Successfully Deleted')
        return reverse_lazy('configuration:ReviewRatingListView')




class SupervisorListView(ListView):
    model = Supervisor
    template_name = 'configuration/supervisor/supervisor_list.html'
    context_object_name = 'supervisors'

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(SupervisorListView, self).get_context_data(**kwargs)
        context['data'] = userdata
        context['employee'] = self.model.objects.all()
        return context

class SupervisorCreateView(CreateView):
    model = Supervisor
    form_class = SupervisorForm
    template_name = 'configuration/supervisor/supervisor_add.html'
    success_url = reverse_lazy('configuration:SupervisorListView')

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(SupervisorCreateView, self).get_context_data(**kwargs)
        context['data'] = userdata
        context['form'] = self.form_class
        return context

    def form_valid(self, form):
        print(form)
        if form.is_valid:
            supervisor = form.save(commit=False)
            supervisor.created_date = datetime.now()
            supervisor.updated_date = datetime.now()
            supervisor.created_by_id =self.request.session['id']
            supervisor.updated_by_id =self.request.session['id']
            supervisor.save()
            messages.success(self.request, 'Data Successfully Saved')
            return super(SupervisorCreateView, self).form_valid(form)
        else:
            messages.error(self.request, 'invalid')
            return super(SupervisorCreateView, self).form_invalid(form)

class SupervisorUpdateView(UpdateView):
    model = Supervisor
    form_class = SupervisorForm
    template_name = 'configuration/supervisor/supervisor_update.html'
    success_url = reverse_lazy('configuration:SupervisorListView')
    context_object_name = 'supervisors'

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(SupervisorUpdateView, self).get_context_data(**kwargs)
        context['data'] = userdata
        # context['form'] = self.form_class
        return context

    def form_valid(self, form):

        if form.is_valid:
            supervisor = form.save(commit=False)
            supervisor.updated_by_id =self.request.session['id']
            supervisor.updated_date = datetime.now()
            supervisor.save()
            messages.success(self.request, 'Data Successfully Updated')
            return super(SupervisorUpdateView, self).form_valid(form)
        else:
            messages.error(self.request, 'invalid')
            return super(SupervisorUpdateView, self).form_invalid(form)


class SupervisorDeleteView(DeleteView):
    model = Supervisor
    template_name = 'configuration/supervisor/supervisor_delete.html'
    success_url = reverse_lazy('configuration:SupervisorListView')

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(SupervisorDeleteView, self).get_context_data(**kwargs)
        context['data'] = userdata
        return context

    def get_success_url(self):
        messages.success(self.request, 'Data Successfully Deleted')
        return reverse_lazy('configuration:SupervisorListView')


class ProjectListView(ListView):
    model = Project
    template_name = 'configuration/project/project_list.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['data'] = userdata
        context['employee'] = self.model.objects.all()
        return context

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'configuration/project/project_add.html'
    success_url = reverse_lazy('configuration:ProjectListView')

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(ProjectCreateView, self).get_context_data(**kwargs)
        context['data'] = userdata
        context['form'] = self.form_class
        return context

    def form_valid(self, form):
        print(form)
        if form.is_valid:
            project = form.save(commit=False)
            project.created_date = datetime.now()
            project.updated_date = datetime.now()
            project.created_by_id =self.request.session['id']
            project.updated_by_id =self.request.session['id']
            project.save()
            messages.success(self.request, 'Data Successfully Saved')
            return super(ProjectCreateView, self).form_valid(form)
        else:
            messages.error(self.request, 'invalid')
            return super(ProjectCreateView, self).form_invalid(form)

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'configuration/project/project_update.html'
    success_url = reverse_lazy('configuration:ProjectListView')
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(ProjectUpdateView, self).get_context_data(**kwargs)
        context['data'] = userdata
        # context['form'] = self.form_class
        return context

    def form_valid(self, form):

        if form.is_valid:
            project = form.save(commit=False)
            project.updated_by_id =self.request.session['id']
            project.updated_date = datetime.now()
            project.save()
            messages.success(self.request, 'Data Successfully Updated')
            return super(ProjectUpdateView, self).form_valid(form)
        else:
            messages.error(self.request, 'invalid')
            return super(ProjectUpdateView, self).form_invalid(form)


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'configuration/project/project_delete.html'
    success_url = reverse_lazy('configuration:ProjectListView')

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(ProjectDeleteView, self).get_context_data(**kwargs)
        context['data'] = userdata
        return context

    def get_success_url(self):
        messages.success(self.request, 'Data Successfully Deleted')
        return reverse_lazy('configuration:ProjectListView')


class SBUListView(ListView):
    model = SBU
    template_name = 'configuration/sbu/sbu_list.html'
    context_object_name = 'sbus'

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(SBUListView, self).get_context_data(**kwargs)
        context['data'] = userdata
        context['employee'] = self.model.objects.all()
        return context

class SBUCreateView(CreateView):
    model = SBU
    form_class = SBUForm
    template_name = 'configuration/sbu/sbu_add.html'
    success_url = reverse_lazy('configuration:SBUListView')

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(SBUCreateView, self).get_context_data(**kwargs)
        context['data'] = userdata
        context['form'] = self.form_class
        return context

    def form_valid(self, form):
        print(form)
        if form.is_valid:
            sbu = form.save(commit=False)
            sbu.created_date = datetime.now()
            sbu.updated_date = datetime.now()
            sbu.created_by_id =self.request.session['id']
            sbu.updated_by_id =self.request.session['id']
            sbu.save()
            messages.success(self.request, 'Data Successfully Saved')
            return super(SBUCreateView, self).form_valid(form)
        else:
            messages.error(self.request, 'invalid')
            return super(SBUCreateView, self).form_invalid(form)

class SBUUpdateView(UpdateView):
    model = SBU
    form_class = SBUForm
    template_name = 'configuration/sbu/sbu_update.html'
    success_url = reverse_lazy('configuration:SBUListView')
    context_object_name = 'sbus'

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(SBUUpdateView, self).get_context_data(**kwargs)
        context['data'] = userdata
        # context['form'] = self.form_class
        return context

    def form_valid(self, form):

        if form.is_valid:
            sbu = form.save(commit=False)
            sbu.updated_by_id =self.request.session['id']
            sbu.updated_date = datetime.now()
            sbu.save()
            messages.success(self.request, 'Data Successfully Updated')
            return super(SBUUpdateView, self).form_valid(form)
        else:
            messages.error(self.request, 'invalid')
            return super(SBUUpdateView, self).form_invalid(form)

class SBUDeleteView(DeleteView):
    model = SBU
    template_name = 'configuration/sbu/sbu_delete.html'
    success_url = reverse_lazy('configuration:SBUListView')

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(SBUDeleteView, self).get_context_data(**kwargs)
        context['data'] = userdata
        return context

    def get_success_url(self):
        messages.success(self.request, 'Data Successfully Deleted')
        return reverse_lazy('configuration:SBUListView')



class SubSBUListView(ListView):
    model = SubSBU
    template_name = 'configuration/subsbu/subsbu_list.html'
    context_object_name = 'subsbus'

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(SubSBUListView, self).get_context_data(**kwargs)
        context['data'] = userdata
        context['employee'] = self.model.objects.all()
        return context

class SubSBUCreateView(CreateView):
    model = SubSBU
    form_class = SubSBUForm
    template_name = 'configuration/subsbu/subsbu_add.html'
    success_url = reverse_lazy('configuration:SubSBUListView')

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(SubSBUCreateView, self).get_context_data(**kwargs)
        context['data'] = userdata
        context['form'] = self.form_class
        return context

    def form_valid(self, form):
        print(form)
        if form.is_valid:
            sbusbu = form.save(commit=False)
            sbusbu.created_date = datetime.now()
            sbusbu.updated_date = datetime.now()
            sbusbu.created_by_id =self.request.session['id']
            sbusbu.updated_by_id =self.request.session['id']
            sbusbu.save()
            messages.success(self.request, 'Data Successfully Saved')
            return super(SubSBUCreateView, self).form_valid(form)
        else:
            messages.error(self.request, 'invalid')
            return super(SubSBUCreateView, self).form_invalid(form)

class SubSBUUpdateView(UpdateView):
    model = SubSBU
    form_class = SubSBUForm
    template_name = 'configuration/subsbu/subsbu_update.html'
    success_url = reverse_lazy('configuration:SubSBUListView')
    context_object_name = 'subsbus'

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(SubSBUUpdateView, self).get_context_data(**kwargs)
        context['data'] = userdata
        # context['form'] = self.form_class
        return context

    def form_valid(self, form):

        if form.is_valid:
            subsbu = form.save(commit=False)
            subsbu.updated_by_id =self.request.session['id']
            subsbu.updated_date = datetime.now()
            subsbu.save()
            messages.success(self.request, 'Data Successfully Updated')
            return super(SubSBUUpdateView, self).form_valid(form)
        else:
            messages.error(self.request, 'invalid')
            return super(SubSBUUpdateView, self).form_invalid(form)

class SubSBUDeleteView(DeleteView):
    model = SubSBU
    template_name = 'configuration/subsbu/subsbu_delete.html'
    success_url = reverse_lazy('configuration:SubSBUListView')

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(SubSBUDeleteView, self).get_context_data(**kwargs)
        context['data'] = userdata
        return context

    def get_success_url(self):
        messages.success(self.request, 'Data Successfully Deleted')
        return reverse_lazy('configuration:SubSBUListView')



class KPIObjectiveListView(ListView):
    model = KPIObjective
    template_name = 'configuration/kpiobjective/kpiobjective_list.html'
    context_object_name = 'kpiobjectives'

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(KPIObjectiveListView, self).get_context_data(**kwargs)
        context['data'] = userdata
        context['employee'] = self.model.objects.all()
        return context

class KPIObjectiveCreateView(CreateView):
    model = KPIObjective
    form_class = KPIObjectiveForm
    template_name = 'configuration/kpiobjective/kpiobjective_add.html'
    success_url = reverse_lazy('configuration:KPIObjectiveListView')

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(KPIObjectiveCreateView, self).get_context_data(**kwargs)
        context['data'] = userdata
        context['form'] = self.form_class
        return context

    def form_valid(self, form):
        print(form)
        if form.is_valid:
            kpiobjective = form.save(commit=False)
            kpiobjective.created_date = datetime.now()
            kpiobjective.updated_date = datetime.now()
            kpiobjective.created_by_id =self.request.session['id']
            kpiobjective.updated_by_id =self.request.session['id']
            kpiobjective.save()
            messages.success(self.request, 'Data Successfully Saved')
            return super(KPIObjectiveCreateView, self).form_valid(form)
        else:
            messages.error(self.request, 'invalid')
            return super(KPIObjectiveCreateView, self).form_invalid(form)

class KPIObjectiveUpdateView(UpdateView):
    model = KPIObjective
    form_class = KPIObjectiveForm
    template_name = 'configuration/kpiobjective/kpiobjective_update.html'
    success_url = reverse_lazy('configuration:KPIObjectiveListView')
    context_object_name = 'subsbus'

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(KPIObjectiveUpdateView, self).get_context_data(**kwargs)
        context['data'] = userdata
        # context['form'] = self.form_class
        return context

    def form_valid(self, form):

        if form.is_valid:
            kpiobjective = form.save(commit=False)
            kpiobjective.updated_by_id =self.request.session['id']
            kpiobjective.updated_date = datetime.now()
            kpiobjective.save()
            messages.success(self.request, 'Data Successfully Updated')
            return super(KPIObjectiveUpdateView, self).form_valid(form)
        else:
            messages.error(self.request, 'invalid')
            return super(KPIObjectiveUpdateView, self).form_invalid(form)

class KPIObjectiveDeleteView(DeleteView):
    model = KPIObjective
    template_name = 'configuration/kpiobjective/kpiobjective_delete.html'
    # success_url = reverse_lazy('configuration:KPIObjectiveListView')

    def get_context_data(self, **kwargs):
        userdata = {
            'user_id': self.request.session['id'],
            'username': self.request.session['username'],
            'urls': self.request.session['urls'],
        }
        context = super(KPIObjectiveDeleteView, self).get_context_data(**kwargs)
        context['data'] = userdata
        return context

    def get_success_url(self):
        messages.success(self.request, 'Data Successfully Deleted')
        return reverse_lazy('configuration:KPIObjectiveListView')
