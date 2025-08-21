from django.test import TestCase
from django.urls import reverse
from accounts.models import User
from app.models import Syllabus


class SyllabusViewTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", email="user1@gmail.com", password="pass123")
        self.user2 = User.objects.create_user(username="user2", email="user2@gmail.com", password="pass123")

        self.syllabus1 = Syllabus.objects.create(name="Math", user=self.user1)
        self.syllabus2 = Syllabus.objects.create(name="Science", user=self.user2)

    
    def test_list_view_requires_login(self):
        response = self.client.get(reverse("syllabus-list"))
        self.assertNotEqual(response.status_code, 200)  

    def test_list_view_shows_only_own_syllabuses(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.get(reverse("syllabus-list"))
        syllabuses = response.context["syllabuses"]
        self.assertIn(self.syllabus1, syllabuses)
        self.assertNotIn(self.syllabus2, syllabuses)

   
    def test_create_view_adds_syllabus_with_user(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("syllabus-create"), {"name": "History"})
        self.assertRedirects(response, reverse("syllabus-list"))
        self.assertTrue(Syllabus.objects.filter(name="History", user=self.user1).exists())

    
    def test_update_view_allows_owner(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(
            reverse("syllabus-update", args=[self.syllabus1.id]),
            {"name": "Updated Math"}
        )
        self.assertRedirects(response, reverse("syllabus-list"))
        self.syllabus1.refresh_from_db()
        self.assertEqual(self.syllabus1.name, "Updated Math")

    def test_update_view_forbidden_for_other_users(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(
            reverse("syllabus-update", args=[self.syllabus2.id]),
            {"name": "Hack Science"}
        )
        self.assertEqual(response.status_code, 404)

  
    def test_delete_view_allows_owner(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("syllabus-delete", args=[self.syllabus1.id]))
        self.assertRedirects(response, reverse("syllabus-list"))
        self.assertFalse(Syllabus.objects.filter(id=self.syllabus1.id).exists())

    def test_delete_view_forbidden_for_other_users(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("syllabus-delete", args=[self.syllabus2.id]))
        self.assertEqual(response.status_code, 404)
