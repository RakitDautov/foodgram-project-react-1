from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from users.models import User


class RegistrationTestCase(APITestCase):

    data = {
        "username": "user",
        "email": "u@mail.com",
        "password": "password"
    }

    def test_registration(self):

        """Тест создания нового пользователя
        post('/api/users/')"""

        response = self.client.post("/api/users/", self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_auth(self):

        """Тест получения токена по email и password
        post('/auth/token/login/')"""

        self.user = User.objects.create_user(
            username=self.data["username"],
            email=self.data["email"],
            password=self.data["password"],
        )

        response = self.client.post("/api/auth/token/login/", self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileTestCase(APITestCase):

    def setUp(self):
        self.user_1 = User.objects.create_user(
            username="user1",
            email="1@mail.ru",
            password="password",
        )
        self.user_2 = User.objects.create_user(
            username="user2",
            email="2@mail.ru",
            password="password",
        )
        self.token = Token.objects.create(user=self.user_1)
        self.api_authentication()

    def api_authentication(self):

        """Функция авторизует пользователя"""

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_profile_information(self):

        """Тест получения информации пользователя"""

        profile_id = {
            "my_profile": "/api/users/me/",
            "profile_1": "/api/users/1/",
            "profile_2": "/api/users/2/",
        }
        for profile, t_id in profile_id.items():
            with self.subTest(t_id=t_id):
                response = self.client.get(t_id)
                self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subscriptions(self):

        """Тест подписки на драгого пользователя"""

        response = self.client.post("/api/users/subscribe/")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
