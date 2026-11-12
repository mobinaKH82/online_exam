from django.db import models
from attempts.models import Attempt
from django.conf import settings

class Appeal(models.Model):

    STATUS_CHOICES = [
        ('pending', 'در انتظار بررسی'),
        ('accepted', 'پذیرفته شده'),
        ('rejected', 'رد شده'),
    ]

    attempt = models.OneToOneField(
        Attempt,
        on_delete=models.CASCADE,
        related_name='appeal'
    )

    reason = models.TextField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

    teacher_response = models.TextField(
        blank=True
    )

    new_score = models.FloatField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    responded_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"اعتراض {self.attempt.student.username} - {self.attempt.exam.title}"


class Notification(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications'
    )

    message = models.TextField()

    appeal = models.ForeignKey(
        Appeal,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notifications'
    )

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"اعلان برای {self.user.username}"