<<<<<<< HEAD
from django.test import TestCase
from django.urls import reverse
from accounts.models import User


class AccountsViewTests(TestCase):

    def test_register_view_creates_user(self):
        response = self.client.post(reverse("register"), {
            "username": "newuser",
            "email": "newuser@example.com",
            "password1": "StrongPass123",
            "password2": "StrongPass123"
        })
       
        self.assertRedirects(response, reverse("syllabus-list"))
     
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login_view_authenticates_user(self):
  
        User.objects.create_user(username="testuser", email="test@example.com", password="pass123")
        response = self.client.post(reverse("login"), {
            "username": "testuser",
            "password": "pass123"
        })
        self.assertRedirects(response, reverse("syllabus-list"))
    
        user = response.wsgi_request.user
        self.assertTrue(user.is_authenticated)
        self.assertEqual(user.username, "testuser")

    def test_logout_view_logs_out_user(self):

        user = User.objects.create_user(username="logoutuser", password="pass123")
        self.client.login(username="logoutuser", password="pass123")
        response = self.client.get(reverse("logout"))
        self.assertRedirects(response, reverse("login"))
 
        user = response.wsgi_request.user
        self.assertFalse(user.is_authenticated)

    def test_register_view_invalid_data(self):
    
        response = self.client.post(reverse("register"), {
            "username": "baduser",
            "email": "bad@example.com",
            "password1": "pass123",
            "password2": "pass456"
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'password2', "The two password fields didn’t match.")
        self.assertFalse(User.objects.filter(username="baduser").exists())

    def test_login_view_invalid_credentials(self):
        response = self.client.post(reverse("login"), {
            "username": "nonexistent",
            "password": "wrongpass"
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', None, "Please enter a correct username and password. Note that both fields may be case-sensitive.")
=======
>>>>>>> 30d0b5d (updated)
