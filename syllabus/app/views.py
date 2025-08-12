from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Syllabus, Subject, Chapter, Topic, Subtopic, StudySession, Revision,  ProgressReport

class SyllabusListView(ListView):
    model = Syllabus
    template_name = 'list.html'
    context_object_name = 'syllabuses'


class SyllabusCreateView(CreateView):
    model = Syllabus
    template_name = 'form.html'
    fields = ['name', 'user']
    success_url = reverse_lazy('syllabus-list')


class SyllabusUpdateView(UpdateView):
    model = Syllabus
    template_name = 'update.html'
    fields = ['name', 'user']
    success_url = reverse_lazy('syllabus-list')


class SyllabusDeleteView(DeleteView):
    model = Syllabus
    template_name = 'delete.html'
    success_url = reverse_lazy('syllabus-list')
    

class SubjectListView(ListView):
    model = Subject
    template_name = 'list.html'
    context_object_name = 'subjects'


class SubjectCreateView(CreateView):
    model = Subject
    template_name = 'form.html'
    fields = ['name', 'syllabus', 'goal_hour']
    success_url = reverse_lazy('subject-list')


class SubjectUpdateView(UpdateView):
    model = Subject
    template_name = 'update.html'
    fields = ['name', 'syllabus', 'goal_hour']
    success_url = reverse_lazy('subject-list')


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'delete.html'
    success_url = reverse_lazy('subject-list')


class ChapterListView(ListView):
    model = Chapter
    template_name = 'list.html'
    context_object_name = 'chapters'


class ChapterCreateView(CreateView):
    model = Chapter
    template_name = 'form.html'
    fields = ['title', 'subject']
    success_url = reverse_lazy('chapter-list')


class ChapterUpdateView(UpdateView):
    model = Chapter
    template_name = 'update.html'
    fields = ['title', 'subject']
    success_url = reverse_lazy('chapter-list')


class ChapterDeleteView(DeleteView):
    model = Chapter
    template_name = 'delete.html'
    success_url = reverse_lazy('chapter-list')


class TopicListView(ListView):
    model = Topic
    template_name = 'list.html'
    context_object_name = 'topics'


class TopicCreateView(CreateView):
    model = Topic
    template_name = 'form.html'
    fields = ['title', 'chapter']
    success_url = reverse_lazy('topic-list')


class TopicUpdateView(UpdateView):
    model = Topic
    template_name = 'update.html'
    fields = ['title', 'chapter']
    success_url = reverse_lazy('topic-list')


class TopicDeleteView(DeleteView):
    model = Topic
    template_name = 'delete.html'
    success_url = reverse_lazy('topic-list')


class SubtopicListView(ListView):
    model = Subtopic
    template_name = 'list.html'
    context_object_name = 'subtopics'


class SubtopicCreateView(CreateView):
    model = Subtopic
    template_name = 'form.html'
    fields = ['title', 'topic']
    success_url = reverse_lazy('subtopic-list')


class SubtopicUpdateView(UpdateView):
    model = Subtopic
    template_name = 'update.html'
    fields = ['title', 'topic']
    success_url = reverse_lazy('subtopic-list')


class SubtopicDeleteView(DeleteView):
    model = Subtopic
    template_name = 'delete.html'
    success_url = reverse_lazy('subtopic-list')


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