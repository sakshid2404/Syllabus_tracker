from django.test import TestCase
from django.urls import reverse
from accounts.models import User
from app.models import Syllabus
from subject.models import Subject, Chapter, Topic, Subtopic


class BaseSetup(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", email="user1@gmail.com", password="pass123")
        self.user2 = User.objects.create_user(username="user2", email="user2@gmail.com", password="pass123")

        self.syllabus1 = Syllabus.objects.create(name="Syllabus 1", user=self.user1)
        self.syllabus2 = Syllabus.objects.create(name="Syllabus 2", user=self.user2)


class SubjectViewTests(BaseSetup):
    def setUp(self):
        super().setUp()
        self.subject1 = Subject.objects.create(name="Math", syllabus=self.syllabus1, goal_hour=10)
        self.subject2 = Subject.objects.create(name="Physics", syllabus=self.syllabus2, goal_hour=12)

    def test_list_view_requires_login(self):
        response = self.client.get(reverse("subject-list"))
        self.assertNotEqual(response.status_code, 200)

    def test_list_view_shows_only_own_subjects(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.get(reverse("subject-list"))
        subjects = response.context["subjects"]
        self.assertIn(self.subject1, subjects)
        self.assertNotIn(self.subject2, subjects)

    def test_create_view_adds_subject_with_syllabus(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("subject-create"), {
            "name": "Biology",
            "syllabus": self.syllabus1.id,
            "goal_hour": 5
        })
        self.assertRedirects(response, reverse("subject-list"))
        self.assertTrue(Subject.objects.filter(name="Biology", syllabus=self.syllabus1).exists())

    def test_update_view_allows_owner(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("subject-update", args=[self.subject1.id]), {
            "name": "Advanced Math",
            "syllabus": self.syllabus1.id,
            "goal_hour": 15
        })
        self.assertRedirects(response, reverse("subject-list"))
        self.subject1.refresh_from_db()
        self.assertEqual(self.subject1.name, "Advanced Math")

    def test_update_view_forbidden_for_other_users(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("subject-update", args=[self.subject2.id]), {
            "name": "Hack Physics",
            "syllabus": self.syllabus1.id,
            "goal_hour": 20
        })
        self.assertEqual(response.status_code, 404)

    def test_delete_view_allows_owner(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("subject-delete", args=[self.subject1.id]))
        self.assertRedirects(response, reverse("subject-list"))
        self.assertFalse(Subject.objects.filter(id=self.subject1.id).exists())

    def test_delete_view_forbidden_for_other_users(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("subject-delete", args=[self.subject2.id]))
        self.assertEqual(response.status_code, 404)


class ChapterViewTests(BaseSetup):
    def setUp(self):
        super().setUp()
        self.subject1 = Subject.objects.create(name="Math", syllabus=self.syllabus1, goal_hour=10)
        self.subject2 = Subject.objects.create(name="Physics", syllabus=self.syllabus2, goal_hour=12)
        self.chapter1 = Chapter.objects.create(title="Algebra", subject=self.subject1)
        self.chapter2 = Chapter.objects.create(title="Mechanics", subject=self.subject2)

    def test_list_view_shows_only_own_chapters(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.get(reverse("chapter-list"))
        chapters = response.context["chapters"]
        self.assertIn(self.chapter1, chapters)
        self.assertNotIn(self.chapter2, chapters)

    def test_create_view_adds_chapter_with_subject(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("chapter-create"), {
            "title": "Geometry",
            "subject": self.subject1.id
        })
        self.assertRedirects(response, reverse("chapter-list"))
        self.assertTrue(Chapter.objects.filter(title="Geometry", subject=self.subject1).exists())

    def test_update_view_allows_owner(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("chapter-update", args=[self.chapter1.id]), {
            "title": "Advanced Algebra",
            "subject": self.subject1.id
        })
        self.assertRedirects(response, reverse("chapter-list"))
        self.chapter1.refresh_from_db()
        self.assertEqual(self.chapter1.title, "Advanced Algebra")

    def test_update_view_forbidden_for_other_users(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("chapter-update", args=[self.chapter2.id]), {
            "title": "Hack Mechanics",
            "subject": self.subject1.id
        })
        self.assertEqual(response.status_code, 404)

    def test_delete_view_allows_owner(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("chapter-delete", args=[self.chapter1.id]))
        self.assertRedirects(response, reverse("chapter-list"))
        self.assertFalse(Chapter.objects.filter(id=self.chapter1.id).exists())

    def test_delete_view_forbidden_for_other_users(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("chapter-delete", args=[self.chapter2.id]))
        self.assertEqual(response.status_code, 404)


class TopicViewTests(BaseSetup):
    def setUp(self):
        super().setUp()
        self.subject1 = Subject.objects.create(name="Math", syllabus=self.syllabus1, goal_hour=10)
        self.chapter1 = Chapter.objects.create(title="Algebra", subject=self.subject1)
        self.chapter2 = Chapter.objects.create(title="Mechanics", subject=Subject.objects.create(name="Physics", syllabus=self.syllabus2, goal_hour=12))
        self.topic1 = Topic.objects.create(title="Linear Equations", chapter=self.chapter1)
        self.topic2 = Topic.objects.create(title="Dynamics", chapter=self.chapter2)

    def test_list_view_shows_only_own_topics(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.get(reverse("topic-list"))
        topics = response.context["topics"]
        self.assertIn(self.topic1, topics)
        self.assertNotIn(self.topic2, topics)

    def test_create_view_adds_topic_with_chapter(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("topic-create"), {
            "title": "Quadratic Equations",
            "chapter": self.chapter1.id
        })
        self.assertRedirects(response, reverse("topic-list"))
        self.assertTrue(Topic.objects.filter(title="Quadratic Equations", chapter=self.chapter1).exists())

    def test_update_view_allows_owner(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("topic-update", args=[self.topic1.id]), {
            "title": "Advanced Linear Equations",
            "chapter": self.chapter1.id
        })
        self.assertRedirects(response, reverse("topic-list"))
        self.topic1.refresh_from_db()
        self.assertEqual(self.topic1.title, "Advanced Linear Equations")

    def test_update_view_forbidden_for_other_users(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("topic-update", args=[self.topic2.id]), {
            "title": "Hack Dynamics",
            "chapter": self.chapter1.id
        })
        self.assertEqual(response.status_code, 404)

    def test_delete_view_allows_owner(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("topic-delete", args=[self.topic1.id]))
        self.assertRedirects(response, reverse("topic-list"))
        self.assertFalse(Topic.objects.filter(id=self.topic1.id).exists())

    def test_delete_view_forbidden_for_other_users(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("topic-delete", args=[self.topic2.id]))
        self.assertEqual(response.status_code, 404)


class SubtopicViewTests(BaseSetup):
    def setUp(self):
        super().setUp()
        self.subject1 = Subject.objects.create(name="Math", syllabus=self.syllabus1, goal_hour=10)
        self.chapter1 = Chapter.objects.create(title="Algebra", subject=self.subject1)
        self.topic1 = Topic.objects.create(title="Linear Equations", chapter=self.chapter1)
        self.topic2 = Topic.objects.create(title="Dynamics", chapter=Chapter.objects.create(title="Mechanics", subject=Subject.objects.create(name="Physics", syllabus=self.syllabus2, goal_hour=12)))
        self.subtopic1 = Subtopic.objects.create(title="Solving Equations", topic=self.topic1)
        self.subtopic2 = Subtopic.objects.create(title="Force Analysis", topic=self.topic2)

    def test_list_view_shows_only_own_subtopics(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.get(reverse("subtopic-list"))
        subtopics = response.context["subtopics"]
        self.assertIn(self.subtopic1, subtopics)
        self.assertNotIn(self.subtopic2, subtopics)

    def test_create_view_adds_subtopic_with_topic(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("subtopic-create"), {
            "title": "Graph Method",
            "topic": self.topic1.id
        })
        self.assertRedirects(response, reverse("subtopic-list"))
        self.assertTrue(Subtopic.objects.filter(title="Graph Method", topic=self.topic1).exists())

    def test_update_view_allows_owner(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("subtopic-update", args=[self.subtopic1.id]), {
            "title": "Advanced Solving Equations",
            "topic": self.topic1.id
        })
        self.assertRedirects(response, reverse("subtopic-list"))
        self.subtopic1.refresh_from_db()
        self.assertEqual(self.subtopic1.title, "Advanced Solving Equations")

    def test_update_view_forbidden_for_other_users(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("subtopic-update", args=[self.subtopic2.id]), {
            "title": "Hack Force Analysis",
            "topic": self.topic1.id
        })
        self.assertEqual(response.status_code, 404)

    def test_delete_view_allows_owner(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("subtopic-delete", args=[self.subtopic1.id]))
        self.assertRedirects(response, reverse("subtopic-list"))
        self.assertFalse(Subtopic.objects.filter(id=self.subtopic1.id).exists())

    def test_delete_view_forbidden_for_other_users(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("subtopic-delete", args=[self.subtopic2.id]))
        self.assertEqual(response.status_code, 404)
