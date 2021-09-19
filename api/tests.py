from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(title='first todo', completed=True)

    def test_title_content(self):
        todo = Task.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'first todo')

    def test_completed_content(self):
        todo = Task.objects.get(id=1)
        expected_object_name = True
        self.assertEquals(expected_object_name, True)
