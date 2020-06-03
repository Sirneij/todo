from django.test import TestCase
from .models import Todo
# Create your tests here.


class TodoTestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='First title', content='content here')

    def test_title(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'First title')

    def test_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.content}'
        self.assertEquals(expected_object_name, 'content here')
