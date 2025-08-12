from django.urls import path
from . import views
urlpatterns = [
    
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