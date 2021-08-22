from django.test import TestCase
from django.contrib.auth import get_user_model

""" Test for user creation """


class UserTests(TestCase):
    """ Test user options """

    def test_create_user_with_succesful(self):
        """Test creating a new user with an email is successful"""
        email = "test@gmail.com"
        password = "changethis"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        # use check_password here because password will be hashed
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized."""
        email = "test@gmail.com"
        user = get_user_model().objects.create_user(email, 'changethis')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user without email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'changethis')

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            'admin@gmail.com',
            'changethis'
        )
        # superuser field is included as part of PermissionsMixin
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
