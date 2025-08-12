from django.urls import path
from . import views
urlpatterns = [
    path('syllabuses/', views.SyllabusListView.as_view(), name='list'),
    path('syllabus/create/', views.SyllabusCreateView.as_view(), name='create'),
    path('syllabus/update/<int:pk>/',views. SyllabusUpdateView.as_view(), name='update'),
    path('syllabus/delete/<int:pk>/', views.SyllabusDeleteView.as_view(), name='delete'),

    
    
]