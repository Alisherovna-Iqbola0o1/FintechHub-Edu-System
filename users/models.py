from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserRole(models.TextChoices):
    ADMIN = "Admin", "Admin"
    TEACHER = "Teacher", "Ustoz"
    STUDENT = "student", "Oquvchi"

class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=UserRole,
        default=UserRole.STUDENT
    )
    phone_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.role