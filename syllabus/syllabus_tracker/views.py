from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import StudySession, Revision,  ProgressReport
from django.contrib.auth.mixins import LoginRequiredMixin


class StudySessionListView(LoginRequiredMixin,ListView):
    model = StudySession
    template_name = 'app/list.html'
    context_object_name = 'study_sessions'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        fields = [field.name for field in self.model._meta.fields]

        object_data = [
            {field: getattr(obj, field) for field in fields}
            for obj in context['object_list']
        ]

        context.update({
            'model_name': self.model._meta.model_name,
            'fields': fields,
            'object_data': object_data,
        })

        return context



class StudySessionCreateView(LoginRequiredMixin,CreateView):
    model = StudySession
    template_name = 'app/form.html'
    fields = ['user', 'topic', 'subtopic', 'date', 'duration_min', 'is_completed']
    success_url = reverse_lazy('studysession-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context



class StudySessionUpdateView(LoginRequiredMixin,UpdateView):
    model = StudySession
    template_name = 'app/update.html'
    fields = ['user', 'topic', 'subtopic', 'date', 'duration_min', 'is_completed']
    success_url = reverse_lazy('studysession-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context



class StudySessionDeleteView(LoginRequiredMixin,DeleteView):
    model = StudySession
    template_name = 'app/delete.html'
    success_url = reverse_lazy('studysession-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context



class RevisionListView(LoginRequiredMixin,ListView):
    model = Revision
    template_name = 'app/list.html'
    context_object_name = 'revisions'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        fields = [field.name for field in self.model._meta.fields]

        object_data = [
            {field: getattr(obj, field) for field in fields}
            for obj in context['object_list']
        ]

        context.update({
            'model_name': self.model._meta.model_name,
            'fields': fields,
            'object_data': object_data,
        })

        return context



class RevisionCreateView(LoginRequiredMixin,CreateView):
    model = Revision
    template_name = 'app/form.html'
    fields = ['user', 'subject', 'topic', 'date', 'revision_type']
    success_url = reverse_lazy('revision-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context



class RevisionUpdateView(LoginRequiredMixin,UpdateView):
    model = Revision
    template_name = 'app/update.html'
    fields = ['user', 'subject', 'topic', 'date', 'revision_type']
    success_url = reverse_lazy('revision-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context



class RevisionDeleteView(LoginRequiredMixin,DeleteView):
    model = Revision
    template_name = 'app/delete.html'
    success_url = reverse_lazy('revision-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context



class ProgressReportListView(LoginRequiredMixin,ListView):
    model = ProgressReport
    template_name = 'app/list.html'
    context_object_name = 'reports'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        fields = [field.name for field in self.model._meta.fields]

        object_data = [
            {field: getattr(obj, field) for field in fields}
            for obj in context['object_list']
        ]

        context.update({
            'model_name': self.model._meta.model_name,
            'fields': fields,
            'object_data': object_data,
        })

        return context



class ProgressReportCreateView(LoginRequiredMixin,CreateView):
    model = ProgressReport
    template_name = 'app/form.html'
    fields = ['user', 'date', 'study_sessions', 'revisions', 'subjects', 'total_study_time', 'total_revision_time']
    success_url = reverse_lazy('progressreport-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context



class ProgressReportUpdateView(LoginRequiredMixin,UpdateView):
    model = ProgressReport
    template_name = 'app/update.html'
    fields = ['user', 'date', 'study_sessions', 'revisions', 'subjects', 'total_study_time', 'total_revision_time']
    success_url = reverse_lazy('progressreport-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context


class ProgressReportDeleteView(LoginRequiredMixin,DeleteView):
    model = ProgressReport
    template_name = 'app/delete.html'
    success_url = reverse_lazy('progressreport-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context
