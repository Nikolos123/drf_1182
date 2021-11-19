from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from .views import AuthorModelViewSet
from .models import Authors, Biography


class TestAuthorViewSet(TestCase):
    url = '/api/authors/'



    # Подготовка тестов
    def setUp(self) -> None:
        pass

    def test_get_list(self):
        # создать объект класса APIRequestFactory
        factory = APIRequestFactory()
        # определяем адрес и метод для отправки запроса
        request = factory.get(self.url)
        # указываем какой тип запроса будет передан в ModelViewSet
        view = AuthorModelViewSet.as_view({'get': 'list'})
        # передаем во вью и получае ответ
        response = view(request)
        # получаем ответ и проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        # создать объект класса APIRequestFactory
        factory = APIRequestFactory()
        # определяем адрес и метод для отправки запроса
        request = factory.post(self.url, {'first_name': 'Александр', 'last_name': 'Пункиш', 'birthday_year': 1799},
                               format='json')
        # указываем какой тип запроса будет передан в ModelViewSet
        view = AuthorModelViewSet.as_view({'post': 'create'})
        # передаем во вью и получае ответ
        response = view(request)
        # получаем ответ и проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        # создать объект класса APIRequestFactory
        factory = APIRequestFactory()
        # определяем адрес и метод для отправки запроса
        request = factory.post(self.url, {'first_name': 'Александр', 'last_name': 'Пункиш', 'birthday_year': 1799},
                               format='json')

        # Создать пользователя под которым будет доступ для создания Автора
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin_12345678')
        # пройти авторизацию с использованием библиотеки force_authenticate
        force_authenticate(request, admin)
        # указываем какой тип запроса будет передан в ModelViewSet
        view = AuthorModelViewSet.as_view({'post': 'create'})
        # передаем во вью и получае ответ
        response = view(request)
        # получаем ответ и проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        # создать объект класса APIClient
        client = APIClient()
        # создать автора через ORM  для проверки детализации
        author = Authors.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
        # запрос
        response = client.get(f'{self.url}{author.id}/')
        # получаем ответ и проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_guest(self):
        # создать объект класса APIClient
        client = APIClient()
        # создать автора через ORM  для проверки детализации
        author = Authors.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
        # запрос
        response = client.put(f'{self.url}{author.id}/',
                              {'first_name': 'Test', 'last_name': 'Test', 'birthday_year': 1799})
        # получаем ответ и проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_admin(self):
        # создать объект класса APIClient
        client = APIClient()
        # создать автора через ORM  для проверки детализации
        author = Authors.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
        # Создать пользователя под которым будет доступ для создания Автора
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin_12345678')
        # залогинится
        client.login(username='admin', password='admin_12345678')
        # запрос
        response = client.put(f'{self.url}{author.id}/',
                              {'first_name': 'Test', 'last_name': 'Test', 'birthday_year': 1111})
        # получаем ответ и проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # получаем автора
        auth = Authors.objects.get(id=author.id)
        # делаем проверку что измениня произошли
        self.assertEqual(auth.first_name, 'Test')
        self.assertEqual(auth.last_name, 'Test')
        self.assertEqual(auth.birthday_year, 1111)
        # Разлогинится
        client.logout()

    def tearDown(self) -> None:
        pass

class TestMath(APISimpleTestCase):

    def test_sqrt(self):
        # импорт модуль
        import math
        # передаем данные в модуль
        response = math.sqrt(4)
        self.assertEqual(response, 2)


    # Очистка

class TestBiographyViewSet(APITestCase):
    url = '/api/biography/'

    def test_get_list(self):
        #делаем запрос
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        # создать автора через ORM  для связи с биографией
        author = Authors.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
        # создали биографию
        bio = Biography.objects.create(text='Test',author=author)
        # Создать пользователя под которым будет доступ для создания Автора
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin_12345678')
        # залогинится
        self.client.login(username='admin', password='admin_12345678')
        # запрос
        response = self.client.put(f'{self.url}{bio.id}/',
                              {'text': 'Биографи', 'author': bio.author.id})
        # получаем ответ и проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # получаем автора
        biog = Biography.objects.get(id=bio.id)
        # делаем проверку что измениня произошли
        self.assertEqual(biog.text, 'Биографи')
        # Разлогинится
        self.client.logout()

    def test_edit_mixer(self):

        # создали биографию
        bio = mixer.blend(Biography)
        # Создать пользователя под которым будет доступ для создания Автора
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin_12345678')
        # залогинится
        self.client.login(username='admin', password='admin_12345678')
        # запрос
        response = self.client.put(f'{self.url}{bio.id}/',
                              {'text': 'Биографи', 'author': bio.author.id})
        # получаем ответ и проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # получаем автора
        biog = Biography.objects.get(id=bio.id)
        # делаем проверку что измениня произошли
        self.assertEqual(biog.text, 'Биографи')
        # Разлогинится
        self.client.logout()


    def test_edit_mixer_text(self):

        # создали биографию
        bio = mixer.blend(Biography,text='Вася')
        self.assertEqual(bio.text, 'Вася')
        # Создать пользователя под которым будет доступ для создания Автора
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin_12345678')
        # залогинится
        self.client.login(username='admin', password='admin_12345678')
        # запрос
        response = self.client.put(f'{self.url}{bio.id}/',
                              {'text': 'Биографи', 'author': bio.author.id})
        # получаем ответ и проверяем код ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # получаем автора
        biog = Biography.objects.get(id=bio.id)
        # делаем проверку что измениня произошли
        self.assertEqual(biog.text, 'Биографи')
        # Разлогинится
        self.client.logout()





