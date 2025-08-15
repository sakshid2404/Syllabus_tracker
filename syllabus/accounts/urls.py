<<<<<<< HEAD
from django.urls import path
from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
=======
>>>>>>> 3d75138126cb3fff9bad839173cb6795ce19e372
