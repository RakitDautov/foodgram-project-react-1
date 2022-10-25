from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from users.models import User, Follow


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

        """Тест получения токена авторизации по email и password
        post('/auth/token/login/')"""

        self.client.post("/api/users/", self.data)
        response = self.client.post("/api/auth/token/login/", self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileTestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_1 = User.objects.create_user(
            username="user1",
            email="1@mail.ru",
            password="password",
        )
        cls.user_1.save()
        cls.user_2 = User.objects.create_user(
            username="user2",
            email="2@mail.ru",
            password="password",
        )
        cls.user_2.save()
        cls.token = Token.objects.create(user=cls.user_1)

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_profile_information(self):

        """Тест получения информации пользователей"""

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

        """Тест подписки на другого пользователя"""

        self.client.post("/api/users/2/subscribe/")
        count = self.client.get("/api/users/subscriptions/").data["count"]
        self.assertEqual(count, 1)

    def test_del_subscriptions(self):

        """Тест удаления подписки на пользователя"""

        self.client.post("/api/users/2/subscribe/")
        self.client.delete("/api/users/2/subscribe/")
        count = self.client.get("/api/users/subscriptions/").data["count"]
        self.assertEqual(count, 0)
