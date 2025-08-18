from django.urls import path
from . import views
urlpatterns = [
    
    path('studysessions/', views. StudySessionListView.as_view(), name='studysession-list'),
    path('studysession/create/', views. StudySessionCreateView.as_view(), name='studysession-create'),
    path('studysession/update/<int:pk>/',views. StudySessionUpdateView.as_view(), name='studysession-update'),
    path('studysession/delete/<int:pk>/', views. StudySessionDeleteView.as_view(), name='studysession-delete'),
    
    path('revisions/',views. RevisionListView.as_view(), name='revision-list'),
    path('revision/create/',views. RevisionCreateView.as_view(), name='revision-create'),
    path('revision/update/<int:pk>/',views.RevisionUpdateView.as_view(), name='revision-update'),
    path('revision/delete/<int:pk>/',views. RevisionDeleteView.as_view(), name='revision-delete'),
    
    
    path('progressreports/', views.ProgressReportListView.as_view(), name='progressreport-list'),
    path('progressreport/create/', views.ProgressReportCreateView.as_view(), name='progressreport-create'),
    path('progressreport/update/<int:pk>/',views.ProgressReportUpdateView.as_view(), name='progressreport-update'),
    path('progressreport/delete/<int:pk>/', views.ProgressReportDeleteView.as_view(), name='progressreport-delete'),
    
]