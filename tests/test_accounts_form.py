from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.forms import CustomUserCreationForm  # Adjust import path as needed

User = get_user_model()


class CustomUserCreationFormTest(TestCase):

    def test_form_valid_with_all_required_fields(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        }

        form = CustomUserCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')

    def test_form_invalid_without_required_email(self):
        form_data = {
            'username': 'testuser',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        }

        form = CustomUserCreationForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)