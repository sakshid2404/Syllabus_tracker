from django.urls import path
from . import views

urlpatterns = [

    
    path('subjects/', views.SubjectListView.as_view(), name='subject-list'),
    path('subject/create/',views. SubjectCreateView.as_view(), name='subject-create'),
    path('subject/update/<int:pk>/', views.SubjectUpdateView.as_view(), name='subject-update'),
    path('subject/delete/<int:pk>/', views.SubjectDeleteView.as_view(), name='subject-delete'),
    
    
    path('chapters/',views. ChapterListView.as_view(), name='chapter-list'),
    path('chapter/create/', views.ChapterCreateView.as_view(), name='chapter-create'),
    path('chapter/update/<int:pk>/',views.ChapterUpdateView.as_view(), name='chapter-update'),
    path('chapter/delete/<int:pk>/',views. ChapterDeleteView.as_view(), name='chapter-delete'),
    
    
    path('topics/',views.TopicListView.as_view(), name='topic-list'),
    path('topic/create/', views.TopicCreateView.as_view(), name='topic-create'),
    path('topic/update/<int:pk>/',views.TopicUpdateView.as_view(), name='topic-update'),
    path('topic/delete/<int:pk>/', views.TopicDeleteView.as_view(), name='topic-delete'),
    
    
    path('subtopics/',views.SubtopicListView.as_view(), name='subtopic-list'),
    path('subtopic/create/',views. SubtopicCreateView.as_view(), name='subtopic-create'),
    path('subtopic/update/<int:pk>/',views.SubtopicUpdateView.as_view(), name='subtopic-update'),
    path('subtopic/delete/<int:pk>/', views.SubtopicDeleteView.as_view(), name='subtopic-delete'),
    
]