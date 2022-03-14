from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from todos.models import Todo


class TestTodoAPI(TestCase):
    """Test Todo endpoint"""

    def setUp(self) -> None:
        super(TestTodoAPI, self).setUp()
        self.user = User.objects.create_user('test_user', 'test@test.com', 'password')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_todo_list(self):
        Todo.objects.create(
            content='test content',
            done=True,
            owner=self.user
        )
        Todo.objects.create(
            content='test content 2',
            done=False,
            owner=self.user
        )

        response = self.client.get(
            reverse('todo-list'),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(2, len(response.data))
        self.assertEqual('test content 2', response.data[0].get('content'))

    def test_get_todo_detail(self):
        Todo.objects.create(
            content='test content',
            done=True,
            owner=self.user
        )

        response = self.client.get(
            '/api/todos/1/'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual('test content', response.data.get('content'))

    def test_create_todo(self):
        data = {
            'content': 'new content'
        }

        response = self.client.post(
            reverse('todo-list'),
            data=data,
            format='json',

        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual('new content', response.data.get('content'))
        self.assertFalse(response.data.get('done'))

    def test_update_todo(self):
        Todo.objects.create(
            content='test content',
            done=True,
            owner=self.user
        )

        data = {
            'content': 'new content',
            'done': False
        }

        response = self.client.put(
            '/api/todos/1/',
            data=data,
            format='json'
        )
        updated_todo = Todo.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('new content', updated_todo.content)
        self.assertFalse(updated_todo.done)

    def test_delete_todo(self):
        Todo.objects.create(
            content='deleted content',
            done=True,
            owner=self.user
        )

        response = self.client.delete(
            '/api/todos/1/'
        )
        updated_todo = Todo.objects.filter(content='deleted content').exists()
        self.assertEqual(response.status_code, 204)
        self.assertFalse(updated_todo)

    def test_filter_completed_todos(self):
        Todo.objects.create(
            content='Todo content',
            done=True,
            owner=self.user
        )

        Todo.objects.create(
            content='Todo different content',
            done=False,
            owner=self.user
        )

        response = self.client.get(
            '/api/todos/?done=true'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Todo content', response.data[0].get('content'))
        self.assertTrue(response.data[0].get('done'))

    def test_filter_todos_by_content(self):
        Todo.objects.create(
            content='Todo content',
            done=False,
            owner=self.user
        )

        Todo.objects.create(
            content='Todo different content',
            done=True,
            owner=self.user
        )

        response = self.client.get(
            '/api/todos/?search=different'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Todo different content', response.data[0].get('content'))
        self.assertTrue(response.data[0].get('done'))
