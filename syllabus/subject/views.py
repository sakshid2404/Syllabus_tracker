from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import  Subject, Chapter, Topic, Subtopic
# Create your views here.


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