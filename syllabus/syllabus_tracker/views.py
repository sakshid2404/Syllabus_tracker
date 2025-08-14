from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import StudySession, Revision,  ProgressReport
from django.contrib.auth.mixins import LoginRequiredMixin


class StudySessionListView(ListView):
    model = StudySession
    template_name = 'app/list.html'
    context_object_name = 'study_sessions'
    

class StudySessionCreateView(LoginRequiredMixin,CreateView):
    model = StudySession
    template_name = 'app/form.html'
    fields = ['user', 'topic', 'subtopic', 'date', 'duration_min', 'is_completed']
    success_url = reverse_lazy('studysession-list')
    
   
class StudySessionUpdateView(LoginRequiredMixin,UpdateView):
    model = StudySession
    template_name = 'app/update.html'
    fields = ['user', 'topic', 'subtopic', 'date', 'duration_min', 'is_completed']
    success_url = reverse_lazy('studysession-list')
  
  
class StudySessionDeleteView(LoginRequiredMixin,DeleteView):
    model = StudySession
    template_name = 'app/delete.html'
    success_url = reverse_lazy('studysession-list')
    

class RevisionListView(LoginRequiredMixin,ListView):
    model = Revision
    template_name = 'app/list.html'
    context_object_name = 'revisions'
    

class RevisionCreateView(LoginRequiredMixin,CreateView):
    model = Revision
    template_name = 'app/form.html'
    fields = ['user', 'subject', 'topic', 'date', 'revision_type']
    success_url = reverse_lazy('revision-list')
    
   
class RevisionUpdateView(LoginRequiredMixin,UpdateView):
    model = Revision
    template_name = 'app/update.html'
    fields = ['user', 'subject', 'topic', 'date', 'revision_type']
    success_url = reverse_lazy('revision-list')
    
   
class RevisionDeleteView(LoginRequiredMixin,DeleteView):
    model = Revision
    template_name = 'app/delete.html'
    success_url = reverse_lazy('revision-list')
    
   
class ProgressReportListView(LoginRequiredMixin,ListView):
    model = ProgressReport
    template_name = 'app/list.html'
    context_object_name = 'reports'
    
  
class ProgressReportCreateView(LoginRequiredMixin,CreateView):
    model = ProgressReport
    template_name = 'app/form.html'
    fields = ['user', 'date', 'study_sessions', 'revisions', 'subjects', 'total_study_time', 'total_revision_time']
    success_url = reverse_lazy('progressreport-list')
  

class ProgressReportUpdateView(LoginRequiredMixin,UpdateView):
    model = ProgressReport
    template_name = 'app/update.html'
    fields = ['user', 'date', 'study_sessions', 'revisions', 'subjects', 'total_study_time', 'total_revision_time']
    success_url = reverse_lazy('progressreport-list')

   
class ProgressReportDeleteView(LoginRequiredMixin,DeleteView):
    model = ProgressReport
    template_name = 'app/delete.html'
    success_url = reverse_lazy('progressreport-list')
    
    