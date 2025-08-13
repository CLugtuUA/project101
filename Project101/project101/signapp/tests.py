from django.test import TestCase
from .models import SignUpRegistration

class SignUpRegistrationModelTest(TestCase):

    def setUp(self):
        self.registration = SignUpRegistration.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            username="johndoe",
            password="password123",
            confirm_password="password123",
            date_of_birth="1990-01-01",
            gender="Male"
        )

    def test_registration_creation(self):
        self.assertEqual(self.registration.first_name, "John")
        self.assertEqual(self.registration.last_name, "Doe")
        self.assertEqual(self.registration.email, "john.doe@example.com")
        self.assertEqual(self.registration.username, "johndoe")
        self.assertEqual(self.registration.date_of_birth.strftime("%Y-%m-%d"), "1990-01-01")
        self.assertEqual(self.registration.gender, "Male")

    def test_email_uniqueness(self):
        with self.assertRaises(Exception):
            SignUpRegistration.objects.create(
                first_name="Jane",
                last_name="Doe",
                email="john.doe@example.com",  # Duplicate email
                username="janedoe",
                password="password456",
                confirm_password="password456",
                date_of_birth="1992-02-02",
                gender="Female"
            )

    def test_passwords_match(self):
        self.assertEqual(self.registration.password, self.registration.confirm_password)