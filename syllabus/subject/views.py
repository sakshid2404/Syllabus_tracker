from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import  Subject, Chapter, Topic, Subtopic
from django.contrib.auth.mixins import LoginRequiredMixin

class SubjectListView(LoginRequiredMixin,ListView):
    model = Subject
    template_name = 'app/list.html'
    context_object_name = 'subjects'
    

<<<<<<< HEAD
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



=======
>>>>>>> be03afdc5e7ce0c27c91f101f3cd38415bd0b938
class SubjectCreateView(LoginRequiredMixin,CreateView):
    model = Subject
    template_name = 'app/form.html'
    fields = ['name', 'syllabus', 'goal_hour']
    success_url = reverse_lazy('subject-list')
    

<<<<<<< HEAD


=======
>>>>>>> be03afdc5e7ce0c27c91f101f3cd38415bd0b938
class SubjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Subject
    template_name = 'app/update.html'
    fields = ['name', 'syllabus', 'goal_hour']
    success_url = reverse_lazy('subject-list')
    

<<<<<<< HEAD


=======
>>>>>>> be03afdc5e7ce0c27c91f101f3cd38415bd0b938
class SubjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Subject
    template_name = 'app/delete.html'
    success_url = reverse_lazy('subject-list')
    

<<<<<<< HEAD


=======
>>>>>>> be03afdc5e7ce0c27c91f101f3cd38415bd0b938
class ChapterListView(LoginRequiredMixin,ListView):
    model = Chapter
    template_name = 'app/list.html'
    context_object_name = 'chapters'
    
<<<<<<< HEAD
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


=======
   
>>>>>>> be03afdc5e7ce0c27c91f101f3cd38415bd0b938
class ChapterCreateView(LoginRequiredMixin,CreateView):
    model = Chapter
    template_name = 'app/form.html'
    fields = ['title', 'subject']
    success_url = reverse_lazy('chapter-list')
    

<<<<<<< HEAD


=======
>>>>>>> be03afdc5e7ce0c27c91f101f3cd38415bd0b938
class ChapterUpdateView(LoginRequiredMixin,UpdateView):
    model = Chapter
    template_name = 'app/update.html'
    fields = ['title', 'subject']
    success_url = reverse_lazy('chapter-list')
    
<<<<<<< HEAD
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context



=======
   
>>>>>>> be03afdc5e7ce0c27c91f101f3cd38415bd0b938
class ChapterDeleteView(LoginRequiredMixin,DeleteView):
    model = Chapter
    template_name = 'app/delete.html'
    success_url = reverse_lazy('chapter-list')
    
<<<<<<< HEAD
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context



=======
   
>>>>>>> be03afdc5e7ce0c27c91f101f3cd38415bd0b938
class TopicListView(LoginRequiredMixin,ListView):
    model = Topic
    template_name = 'app/list.html'
    context_object_name = 'topics'

<<<<<<< HEAD
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



=======
  
>>>>>>> be03afdc5e7ce0c27c91f101f3cd38415bd0b938
class TopicCreateView(LoginRequiredMixin,CreateView):
    model = Topic
    template_name = 'app/form.html'
    fields = ['title', 'chapter']
    success_url = reverse_lazy('topic-list')
<<<<<<< HEAD
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context
LoginRequiredMixin,
=======
>>>>>>> be03afdc5e7ce0c27c91f101f3cd38415bd0b938


class TopicUpdateView(LoginRequiredMixin,UpdateView):
    model = Topic
    template_name = 'app/update.html'
    fields = ['title', 'chapter']
    success_url = reverse_lazy('topic-list')
    
<<<<<<< HEAD
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context



=======
   
>>>>>>> be03afdc5e7ce0c27c91f101f3cd38415bd0b938
class TopicDeleteView(LoginRequiredMixin,DeleteView):
    model = Topic
    template_name = 'app/delete.html'
    success_url = reverse_lazy('topic-list')
    
<<<<<<< HEAD
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context



=======
  
>>>>>>> be03afdc5e7ce0c27c91f101f3cd38415bd0b938
class SubtopicListView(LoginRequiredMixin,ListView):
    model = Subtopic
    template_name = 'app/list.html'
    context_object_name = 'subtopics'
    

<<<<<<< HEAD
    
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



=======
>>>>>>> be03afdc5e7ce0c27c91f101f3cd38415bd0b938
class SubtopicCreateView(LoginRequiredMixin,CreateView):
    model = Subtopic
    template_name = 'app/form.html'
    fields = ['title', 'topic']
    success_url = reverse_lazy('subtopic-list')
    
<<<<<<< HEAD
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context



=======
   
>>>>>>> be03afdc5e7ce0c27c91f101f3cd38415bd0b938
class SubtopicUpdateView(LoginRequiredMixin,UpdateView):
    model = Subtopic
    template_name = 'app/update.html'
    fields = ['title', 'topic']
    success_url = reverse_lazy('subtopic-list')
    

<<<<<<< HEAD


=======
>>>>>>> be03afdc5e7ce0c27c91f101f3cd38415bd0b938
class SubtopicDeleteView(LoginRequiredMixin,DeleteView):
    model = Subtopic
    template_name = 'app/delete.html'
    success_url = reverse_lazy('subtopic-list')
    
   