from django.test import TestCase
from django.conf import settings
from django.test.client import Client

# Create your tests here.

from authapp.models import User

#testCase
class UserManagementTestCase(TestCase):
    username = 'django'
    email = 'django@ya.ru'
    password = 'zaxsew21'

    new_user_data = {
        'username': 'django1',
        'first_name': 'Egorka',
        'last_name': 'Ostr',
        'password1': 'Zartvb32',
        'password2': 'Zartvb32',
        'email': 'gkshp@mail.ru',
        'age':35,
    }


    def setUp(self):
        self.user = User.objects.create_superuser(self.username, email=self.email, password=self.password)
        self.client = Client()


    def test_login(self):
        response = self.client.get('/')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/users/login/')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)


    def test_register(self):
        response = self.client.post('/users/register/', data=self.new_user_data)
        print(response.status_code)
        self.assertEqual(response.status_code, 302)
        new_user = User.objects.get(username=self.new_user_data['username'])
        activation_url = f"{settings.DOMAIN_NAME}/users/verify/{self.new_user_data['email']}/{new_user.activation_key}/"
        response = self.client.get(activation_url)
        print(response.status_code)
        self.assertEqual(response.status_code, 302)
        new_user.refresh_from_db()
        self.assertTrue(new_user.is_active)


    def tearDown(self):
        pass