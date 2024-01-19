from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


# Create your tests here.

class UserTestCase(APITestCase):
    def setUp(self) -> None:
        user = User.objects.create(
            email='test@mail.ru',
            first_name='Test',
            last_name='Test',
            password='12345',
            is_superuser=True
        )
        self.client.force_authenticate(user)
        self.user = user

    def test_create_user(self):
        test_user = {
            'email': 'testemail@mail.ru',
            'password': '12345'
        }
        response = self.client.post(
            '/users/',
            data=test_user
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_user(self):
        User.objects.create(
            email='testemail@mail.ru',
            password='12345'
        )
        update_field = {
            'email': 'newmail@mail.ru'
        }
        response = self.client.patch(
            f'/users/{User.objects.all().last().id}/',
            data=update_field
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
