from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import StudySession, Revision,  ProgressReport


class StudySessionListView(ListView):
    model = StudySession
    template_name = 'list.html'
    context_object_name = 'study_sessions'


class StudySessionCreateView(CreateView):
    model = StudySession
    template_name = 'form.html'
    fields = ['user', 'topic', 'subtopic', 'date', 'duration_min', 'is_completed']
    success_url = reverse_lazy('studysession-list')


class StudySessionUpdateView(UpdateView):
    model = StudySession
    template_name = 'update.html'
    fields = ['user', 'topic', 'subtopic', 'date', 'duration_min', 'is_completed']
    success_url = reverse_lazy('studysession-list')


class StudySessionDeleteView(DeleteView):
    model = StudySession
    template_name = 'delete.html'
    success_url = reverse_lazy('studysession-list')


class RevisionListView(ListView):
    model = Revision
    template_name = 'list.html'
    context_object_name = 'revisions'


class RevisionCreateView(CreateView):
    model = Revision
    template_name = 'form.html'
    fields = ['user', 'subject', 'topic', 'date', 'revision_type']
    success_url = reverse_lazy('revision-list')


class RevisionUpdateView(UpdateView):
    model = Revision
    template_name = 'update.html'
    fields = ['user', 'subject', 'topic', 'date', 'revision_type']
    success_url = reverse_lazy('revision-list')


class RevisionDeleteView(DeleteView):
    model = Revision
    template_name = 'delete.html'
    success_url = reverse_lazy('revision-list')


class ProgressReportListView(ListView):
    model = ProgressReport
    template_name = 'list.html'
    context_object_name = 'progress_reports'


class ProgressReportCreateView(CreateView):
    model = ProgressReport
    template_name = 'form.html'
    fields = ['user', 'date', 'study_sessions', 'revisions', 'subjects', 'total_study_time', 'total_revision_time']
    success_url = reverse_lazy('progressreport-list')


class ProgressReportUpdateView(UpdateView):
    model = ProgressReport
    template_name = 'update.html'
    fields = ['user', 'date', 'study_sessions', 'revisions', 'subjects', 'total_study_time', 'total_revision_time']
    success_url = reverse_lazy('progressreport-list')


class ProgressReportDeleteView(DeleteView):
    model = ProgressReport
    template_name = 'delete.html'
    success_url = reverse_lazy('progressreport-list')