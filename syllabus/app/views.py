from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Syllabus
from django.contrib.auth.mixins import LoginRequiredMixin


class SyllabusListView(LoginRequiredMixin,ListView):
    model = Syllabus
    template_name = 'app/list.html'
    context_object_name = 'syllabuses'
    
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


class SyllabusCreateView(LoginRequiredMixin,CreateView):
    model = Syllabus
    template_name = 'app/form.html'
    fields = ['name', 'user']
    success_url = reverse_lazy('syllabus-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context


class SyllabusUpdateView(LoginRequiredMixin,UpdateView):
    model = Syllabus
    template_name = 'app/update.html'
    fields = ['name', 'user']
    success_url = reverse_lazy('syllabus-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context



class SyllabusDeleteView(LoginRequiredMixin,DeleteView):
    model = Syllabus
    template_name = 'app/delete.html'
    success_url = reverse_lazy('syllabus-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name.title()
        return context



