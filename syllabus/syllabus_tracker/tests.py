from django.test import TestCase
from django.urls import reverse
from accounts.models import User
from app.models import Syllabus
from subject.models import Subject, Chapter, Topic, Subtopic
from syllabus_tracker.models import StudySession, Revision, ProgressReport
from datetime import date

class BaseSetup(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", email="user1@gmail.com", password="pass123")
        self.user2 = User.objects.create_user(username="user2", email="user2@gmail.com", password="pass123")

        self.syllabus1 = Syllabus.objects.create(name="Syllabus 1", user=self.user1)
        self.syllabus2 = Syllabus.objects.create(name="Syllabus 2", user=self.user2)


        self.subject1 = Subject.objects.create(name="Math", syllabus=self.syllabus1, goal_hour=10)
        self.subject2 = Subject.objects.create(name="Physics", syllabus=self.syllabus2, goal_hour=12)


        self.chapter1 = Chapter.objects.create(title="Algebra", subject=self.subject1)
        self.chapter2 = Chapter.objects.create(title="Mechanics", subject=self.subject2)


        self.topic1 = Topic.objects.create(title="Linear Equations", chapter=self.chapter1)
        self.topic2 = Topic.objects.create(title="Dynamics", chapter=self.chapter2)


        self.subtopic1 = Subtopic.objects.create(title="Solving Equations", topic=self.topic1)
        self.subtopic2 = Subtopic.objects.create(title="Force Analysis", topic=self.topic2)


class StudySessionTests(BaseSetup):
    def test_create_study_session(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("studysession-create"), {
            "syllabus": self.syllabus1.id,
            "subject": self.subject1.id,
            "chapter": self.chapter1.id,
            "topic": self.topic1.id,
            "subtopic": self.subtopic1.id,
            "duration_min": 60,
            "is_completed": True
        })
        self.assertRedirects(response, reverse("studysession-list"))
        self.assertTrue(StudySession.objects.filter(subject=self.subject1).exists())

    def test_list_shows_only_own_sessions(self):
        session = StudySession.objects.create(
            syllabus=self.syllabus1, subject=self.subject1,
            chapter=self.chapter1, topic=self.topic1,
            subtopic=self.subtopic1, duration_min=30
        )
        self.client.login(username="user1", password="pass123")
        response = self.client.get(reverse("studysession-list"))
        self.assertIn(session, response.context["study_sessions"])

    def test_update_session(self):
        session = StudySession.objects.create(
            syllabus=self.syllabus1, subject=self.subject1,
            chapter=self.chapter1, topic=self.topic1,
            subtopic=self.subtopic1, duration_min=30
        )
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("studysession-update", args=[session.id]), {
            "subject": self.subject1.id,
            "chapter": self.chapter1.id,
            "topic": self.topic1.id,
            "subtopic": self.subtopic1.id,
            "duration_min": 45,
            "is_completed": True
        })
        self.assertRedirects(response, reverse("studysession-list"))
        session.refresh_from_db()
        self.assertEqual(session.duration_min, 45)
        self.assertTrue(session.is_completed)

    def test_delete_session(self):
        session = StudySession.objects.create(
            syllabus=self.syllabus1, subject=self.subject1,
            chapter=self.chapter1, topic=self.topic1,
            subtopic=self.subtopic1, duration_min=30
        )
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("studysession-delete", args=[session.id]))
        self.assertRedirects(response, reverse("studysession-list"))
        self.assertFalse(StudySession.objects.filter(id=session.id).exists())


class RevisionTests(BaseSetup):
    def test_create_revision(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("revision-create"), {
            "syllabus": self.syllabus1.id,
            "subject": self.subject1.id,
            "chapter": self.chapter1.id,
            "topic": self.topic1.id,
            "subtopic": self.subtopic1.id,
            "date": date.today(),
            "revision_type": "quick"
        })
        self.assertRedirects(response, reverse("revision-list"))
        self.assertTrue(Revision.objects.filter(subject=self.subject1).exists())

    def test_list_shows_only_own_revisions(self):
        rev = Revision.objects.create(
            syllabus=self.syllabus1, subject=self.subject1,
            chapter=self.chapter1, topic=self.topic1,
            subtopic=self.subtopic1, date=date.today(),
            revision_type="quick"
        )
        self.client.login(username="user1", password="pass123")
        response = self.client.get(reverse("revision-list"))
        self.assertIn(rev, response.context["revisions"])


class ProgressReportTests(BaseSetup):
    def test_create_progress_report(self):
        session = StudySession.objects.create(
            syllabus=self.syllabus1, subject=self.subject1,
            chapter=self.chapter1, topic=self.topic1,
            subtopic=self.subtopic1, duration_min=30
        )
        rev = Revision.objects.create(
            syllabus=self.syllabus1, subject=self.subject1,
            chapter=self.chapter1, topic=self.topic1,
            subtopic=self.subtopic1, date=date.today(),
            revision_type="quick"
        )
        self.client.login(username="user1", password="pass123")
        response = self.client.post(reverse("progressreport-create"), {
            "syllabus": self.syllabus1.id,
            "study_sessions": session.id,
            "revisions": rev.id,
            "subjects": self.subject1.id,
            "total_study_time_in_hours": 2,
            "total_revision_time_in_hours": 1
        })
        self.assertRedirects(response, reverse("progressreport-list"))
        self.assertTrue(ProgressReport.objects.filter(subjects=self.subject1).exists())
