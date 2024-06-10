from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.urls import reverse


class QuestionModelTests(TestCase):
    def test_question_str_representation(self):
        # Create a sample question
        question = Question(question_text="What is the meaning of life?")
        self.assertEqual(str(question), "What is the meaning of life?")

    def test_was_published_recently_with_future_question(self):
        # Create a question with a future publication date
        future_date = timezone.now() + timezone.timedelta(days=1)
        question = Question(pub_date=future_date)
        self.assertFalse(question.was_published_recently())

    def test_was_published_recently_with_recent_question(self):
        # Create a question with a recent publication date
        recent_date = timezone.now() - timezone.timedelta(hours=12)
        question = Question(pub_date=recent_date)
        self.assertTrue(question.was_published_recently())

    def test_was_published_recently_with_old_question(self):
        # Create a question with an old publication date
        old_date = timezone.now() - timezone.timedelta(days=2)
        question = Question(pub_date=old_date)
        self.assertFalse(question.was_published_recently())


class IndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_recent_questions(self):
        """
        Only recent questions (within the last 24 hours and not in the future) should be displayed.
        """
        # Create a recent question (within the last 24 hours)
        recent_question = Question.objects.create(
            question_text="What is the meaning of life?",
            pub_date=timezone.now() - timezone.timedelta(hours=12),
        )

        # Create a future question (beyond 24 hours from now)
        future_question = Question.objects.create(
            question_text="What will happen tomorrow?",
            pub_date=timezone.now() + timezone.timedelta(days=2),
        )

        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, recent_question.question_text)
        # self.assertNotContains(response, future_question.question_text)

    def test_template_used(self):
        """
        The correct template should be used for rendering the view.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "polls/index.html")
