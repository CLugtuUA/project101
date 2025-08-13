from django.db import models
from django.core.exceptions import ValidationError

class SignUpRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_registered = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=12, default="")

    def clean(self):
        if self.password != self.confirm_password:
            raise ValidationError("Passwords do not match.")
        if not self.first_name or not self.last_name or not self.email or not self.username or not self.password or not self.confirm_password or not self.date_of_birth:
            raise ValidationError("All fields are required.")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"