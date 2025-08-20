from django.urls import path
from . import views
urlpatterns = [
    path('', views.SyllabusListView.as_view(), name='syllabus-list'),
    path('syllabus/create/', views.SyllabusCreateView.as_view(), name='syllabus-create'),
 
    path('syllabus/update/<int:pk>/',views. SyllabusUpdateView.as_view(), name='syllabus-update'),
    path('syllabus/delete/<int:pk>/', views.SyllabusDeleteView.as_view(), name='syllabus-delete'),

 
]
