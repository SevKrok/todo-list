from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from todo.forms import validate_deadline
from todo.models import Task, Tag

TASK_URL = reverse("todo:task-list")
TAG_URL = reverse("todo:tag-list")


class ViewsTests(TestCase):
    def test_tasks_correct_ordering(self):
        Task.objects.create(
            content="task1",
            created_at=timezone.now(),
            is_completed=False
        )
        Task.objects.create(
            content="task2",
            created_at=timezone.now() - timezone.timedelta(days=1),
            is_completed=False
        )
        Task.objects.create(
            content="task3",
            created_at=timezone.now() - timezone.timedelta(days=2),
            is_completed=False
        )

        response = self.client.get(TASK_URL)
        tasks = Task.objects.all().order_by("is_completed", "-created_at")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks)
        )
        self.assertTemplateUsed(
            response,
            "todo/task_list.html"
        )

    def test_tags_correct_ordering(self):
        Tag.objects.create(name="hello")
        Tag.objects.create(name="goodbye")

        response = self.client.get(TAG_URL)
        tags = Tag.objects.all().order_by("name")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["tag_list"]),
            list(tags)
        )
        self.assertTemplateUsed(
            response,
            "todo/tag_list.html"
        )


class FormsTest(TestCase):
    def test_deadline_validation_with_invalid_data(self):
        with self.assertRaisesMessage(
                ValidationError,
                expected_message=(
                        "Oops! This deadline is not realistic. "
                        "Try picking another time."
                )
        ):
            validate_deadline(timezone.now())
