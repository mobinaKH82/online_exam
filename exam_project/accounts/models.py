
from django.db import models
from django.conf import settings


class Profile(models.Model):

    ROLE_CHOICES = [
        ('student', 'دانشجو'),
        ('teacher', 'استاد'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES
    )

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
