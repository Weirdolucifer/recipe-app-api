from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """testing user creation with an email"""
        email = 'test@gamil.com'
        password = 'password'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalized_email(self):
        """testing the email is normalized"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='123'
        )
        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        """testing a user with no email must raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')

    def test_create_super_user(self):
        """testing a user is superuser or not"""
        user = get_user_model().objects.create_super_user(
            email='test@gmail.com',
            password='123'
            )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
