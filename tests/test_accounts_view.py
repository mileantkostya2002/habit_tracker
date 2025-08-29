from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages

User = get_user_model()


class RegisterViewTest(TestCase):

    def test_register_creates_user_and_shows_success_message(self):
        url = reverse('accounts:register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        }

        response = self.client.post(url, data)

        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertRedirects(response, reverse('accounts:login'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Account for testuser was created! You can now sign in.')
