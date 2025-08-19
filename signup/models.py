from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class SignUpRegistration(models.Model):
    first_name = models.CharField(max_length=100)          # first _ name
    last_name = models.CharField(max_length=100)           # last _ name
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    date_of_birth = models.DateField()                     # date of _ _ birth
    date_registered = models.DateTimeField(auto_now_add=True)  # date _ registered
    gender = models.CharField(max_length=12, default="")

    def clean(self):
        """
        Model-level validation: ensure required fields present and passwords match.
        """
        errors = {}

        # Required fields (Django also enforces because blank=False by default)
        required = ['first_name', 'last_name', 'email', 'username',
                    'password', 'confirm_password', 'date_of_birth']
        for field in required:
            if not getattr(self, field):
                errors[field] = 'This field is required.'

        # Password match check
        if self.password != self.confirm_password:
            errors['confirm_password'] = 'Passwords do not match.'

        # Prevent future birthdates
        if self.date_of_birth and self.date_of_birth > timezone.localdate():
            errors['date_of_birth'] = 'Date of birth cannot be in the future.'

        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        # Enforce validation whenever the model is saved (admin, views, shell, etc.)
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.email})"
