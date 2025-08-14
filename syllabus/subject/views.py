from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import  Subject, Chapter, Topic, Subtopic
from django.contrib.auth.mixins import LoginRequiredMixin


class SubjectListView(ListView):
    model = Subject
    template_name = 'app/list.html'
    context_object_name = 'subjects'
    

class SubjectCreateView(LoginRequiredMixin,CreateView):
    model = Subject
    template_name = 'app/form.html'
    fields = ['name', 'syllabus', 'goal_hour']
    success_url = reverse_lazy('subject-list')
    

class SubjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Subject
    template_name = 'app/update.html'
    fields = ['name', 'syllabus', 'goal_hour']
    success_url = reverse_lazy('subject-list')
    

class SubjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Subject
    template_name = 'app/delete.html'
    success_url = reverse_lazy('subject-list')
    

class ChapterListView(LoginRequiredMixin,ListView):
    model = Chapter
    template_name = 'app/list.html'
    context_object_name = 'chapters'
    
   
class ChapterCreateView(LoginRequiredMixin,CreateView):
    model = Chapter
    template_name = 'app/form.html'
    fields = ['title', 'subject']
    success_url = reverse_lazy('chapter-list')
    

class ChapterUpdateView(LoginRequiredMixin,UpdateView):
    model = Chapter
    template_name = 'app/update.html'
    fields = ['title', 'subject']
    success_url = reverse_lazy('chapter-list')
    
   
class ChapterDeleteView(LoginRequiredMixin,DeleteView):
    model = Chapter
    template_name = 'app/delete.html'
    success_url = reverse_lazy('chapter-list')
    
   
class TopicListView(LoginRequiredMixin,ListView):
    model = Topic
    template_name = 'app/list.html'
    context_object_name = 'topics'

  
class TopicCreateView(LoginRequiredMixin,CreateView):
    model = Topic
    template_name = 'app/form.html'
    fields = ['title', 'chapter']
    success_url = reverse_lazy('topic-list')


class TopicUpdateView(LoginRequiredMixin,UpdateView):
    model = Topic
    template_name = 'app/update.html'
    fields = ['title', 'chapter']
    success_url = reverse_lazy('topic-list')
    
   
class TopicDeleteView(LoginRequiredMixin,DeleteView):
    model = Topic
    template_name = 'app/delete.html'
    success_url = reverse_lazy('topic-list')
    
  
class SubtopicListView(LoginRequiredMixin,ListView):
    model = Subtopic
    template_name = 'app/list.html'
    context_object_name = 'subtopics'
    

class SubtopicCreateView(LoginRequiredMixin,CreateView):
    model = Subtopic
    template_name = 'app/form.html'
    fields = ['title', 'topic']
    success_url = reverse_lazy('subtopic-list')
    
   
class SubtopicUpdateView(LoginRequiredMixin,UpdateView):
    model = Subtopic
    template_name = 'app/update.html'
    fields = ['title', 'topic']
    success_url = reverse_lazy('subtopic-list')
    

class SubtopicDeleteView(LoginRequiredMixin,DeleteView):
    model = Subtopic
    template_name = 'app/delete.html'
    success_url = reverse_lazy('subtopic-list')
    
   