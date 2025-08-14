from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Syllabus
from django.contrib.auth.mixins import LoginRequiredMixin


class SyllabusListView(ListView):
    model = Syllabus
    template_name = 'app/list.html'
    context_object_name = 'syllabuses'
    
    


class SyllabusCreateView(LoginRequiredMixin,CreateView):
    model = Syllabus
    template_name = 'app/form.html'
    fields = ['name', 'user']
    success_url = reverse_lazy('syllabus-list')
    
    

class SyllabusUpdateView(LoginRequiredMixin,UpdateView):
    model = Syllabus
    template_name = 'app/update.html'
    fields = ['name', 'user']
    success_url = reverse_lazy('syllabus-list')
    
    



class SyllabusDeleteView(LoginRequiredMixin,DeleteView):
    model = Syllabus
    template_name = 'app/delete.html'
    success_url = reverse_lazy('syllabus-list')
    
   


