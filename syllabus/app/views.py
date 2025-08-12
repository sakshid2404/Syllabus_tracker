from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Syllabus

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
    



