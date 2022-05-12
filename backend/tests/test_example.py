# Каждый логический набор тестов — это класс,
# который наследуется от базового класса TestCase
from django.test import TestCase


class Test(TestCase):
    def test_example(self):
        # пишем тест тут
        ...