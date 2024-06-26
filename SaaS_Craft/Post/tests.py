from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class SignupTest(TestCase):
    def test_signup_success(self):

        user_data = {
            'username': 'testuser',
            'email': 'text@gmail.com',
            'password':  'testpassword',
            'password2': 'testpassword'
        }


        response = self.client.post(reverse('signup'), user_data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_signup_duplicate_username(self):
        User.objects.create_user(username='testuser', email='exists@gmail.com', password='exists')
        
        user_data = {
            'username': 'testuse',
            'email': 'exists@gmail.com',
            'password': 'testpassword',
            'password2': 'testpasswor'
        }

        response = self.client.post(reverse('signup'), user_data)

        self.assertEqual(response.status_code, 400)
        self.assertFalse(User.objects.filter(email='text@gmail.com').exists())

    def test_is_none(self):

        data = {
            'username' : 'testuse',
            'email' : 'test@gmail.com',
            'password': '1234',
            
        }
        response = self.client.post(reverse('signup'), data)

        self.assertEqual(response.status_code, 400)
        


class LoginTest(TestCase):
    
    def test_authenicate(self):

        data = {
            "username": "test",
            "email": 'test@gmail.com',
            "password": '1234',
            'password2': '1234',
        }

        response = self.client.post(reverse('signup'), data)


        current_user_data = {
            "username": "test",
            "password": "1234"
        }

        respons1 = self.client.post(reverse("signin"), current_user_data)


        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='test').exists())

    def test_user_note_authenticate(self):

       
        
        data = {
            "username": "test",
            "email": 'test@gmail.com',
            "password": '1234',
            'password2': '1234',
        }

        respons = self.client.post(reverse('signin'), data)

        current_user = {
            "username": 'test',
            'password': "123"
        }

        response = self.client.post(reverse('signin'), current_user)

        self.assertEqual(response.status_code, 400)


