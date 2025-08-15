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



class SyllabusCreateView(CreateView):
    model = Syllabus
    fields = ['name'] 
    template_name = 'app/form.html'
    success_url = reverse_lazy('syllabus-list')

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model.__name__
        context['list_url_name'] = 'syllabus-list'
        return context


class SyllabusUpdateView(LoginRequiredMixin,UpdateView):
    model = Syllabus
    template_name = 'app/update.html'
    fields = ['name']
    success_url = reverse_lazy('syllabus-list')    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model.__name__
        context['list_url_name'] = 'syllabus-list'
        return context



class SyllabusDeleteView(LoginRequiredMixin,DeleteView):
    model = Syllabus
    template_name = 'app/delete.html'
    success_url = reverse_lazy('syllabus-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model.__name__
        context['list_url_name'] = 'syllabus-list'
        return context
