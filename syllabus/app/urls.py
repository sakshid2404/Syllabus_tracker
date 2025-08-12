<<<<<<< HEAD
=======
from django.urls import path
from . import views
urlpatterns = [
    path('syllabuses/', views.SyllabusListView.as_view(), name='list'),
    path('syllabus/create/', views.SyllabusCreateView.as_view(), name='create'),
    path('syllabus/update/<int:pk>/',views. SyllabusUpdateView.as_view(), name='update'),
    path('syllabus/delete/<int:pk>/', views.SyllabusDeleteView.as_view(), name='delete'),

    
    
]
>>>>>>> 6a2beae6b079b7ab8e26ec8bcd9888130852c84b
