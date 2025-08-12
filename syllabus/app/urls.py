from django.urls import path
from . import views
urlpatterns = [
    path('syllabuses/', views.SyllabusListView.as_view(), name='list'),
    path('syllabus/create/', views.SyllabusCreateView.as_view(), name='create'),
    path('syllabus/update/<int:pk>/',views. SyllabusUpdateView.as_view(), name='update'),
    path('syllabus/delete/<int:pk>/', views.SyllabusDeleteView.as_view(), name='delete'),

    path('subjects/', views.SubjectListView.as_view(), name='list'),
    path('subject/create/',views. SubjectCreateView.as_view(), name='create'),
    path('subject/update/<int:pk>/', views.SubjectUpdateView.as_view(), name='update'),
    path('subject/delete/<int:pk>/', views.SubjectDeleteView.as_view(), name='delete'),
    
    
    path('chapters/',views. ChapterListView.as_view(), name='list'),
    path('chapter/create/', views.ChapterCreateView.as_view(), name='create'),
    path('chapter/update/<int:pk>/',views.ChapterUpdateView.as_view(), name='update'),
    path('chapter/delete/<int:pk>/',views. ChapterDeleteView.as_view(), name='delete'),
    
    
    path('topics/',views.TopicListView.as_view(), name='list'),
    path('topic/create/', views.TopicCreateView.as_view(), name='create'),
    path('topic/update/<int:pk>/',views.TopicUpdateView.as_view(), name='update'),
    path('topic/delete/<int:pk>/', views.TopicDeleteView.as_view(), name='delete'),
    
    
    path('subtopics/',views.SubtopicListView.as_view(), name='list'),
    path('subtopic/create/',views. SubtopicCreateView.as_view(), name='create'),
    path('subtopic/update/<int:pk>/',views.SubtopicUpdateView.as_view(), name='update'),
    path('subtopic/delete/<int:pk>/', views.SubtopicDeleteView.as_view(), name='delete'),
    
    
    path('studysessions/', views. StudySessionListView.as_view(), name='list'),
    path('studysession/create/', views. StudySessionCreateView.as_view(), name='create'),
    path('studysession/update/<int:pk>/',views. StudySessionUpdateView.as_view(), name='update'),
    path('studysession/delete/<int:pk>/', views. StudySessionDeleteView.as_view(), name='delete'),
    
    
    path('revisions/',views. RevisionListView.as_view(), name='list'),
    path('revision/create/',views. RevisionCreateView.as_view(), name='create'),
    path('revision/update/<int:pk>/',views.RevisionUpdateView.as_view(), name='update'),
    path('revision/delete/<int:pk>/',views. RevisionDeleteView.as_view(), name='delete'),
    
    
    path('progressreports/', views.ProgressReportListView.as_view(), name='list'),
    path('progressreport/create/', views.ProgressReportCreateView.as_view(), name='create'),
    path('progressreport/update/<int:pk>/',views.ProgressReportUpdateView.as_view(), name='update'),
    path('progressreport/delete/<int:pk>/', views.ProgressReportDeleteView.as_view(), name='delete'),
    
]