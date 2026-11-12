from django.db import models
from django.conf import settings
from exams.models import Exam, Question, Choice

class Attempt(models.Model):

    STATUS_CHOICES = [
        ('in_progress', 'در حال برگزاری'),
        ('submitted', 'ارسال شده'),
        ('auto_submitted', 'ارسال خودکار'),
    ]

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='attempts'
    )

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name='attempts'
    )

    started_at = models.DateTimeField()

    deadline = models.DateTimeField()

    finished_at = models.DateTimeField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='in_progress'
    )

    score = models.FloatField(
        null=True,
        blank=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'exam'],
                name='unique_student_exam_attempt'
            )
        ]

    def __str__(self):
        return f"{self.student.username} - {self.exam.title}"


class Answer(models.Model):

    attempt = models.ForeignKey(
        Attempt,
        on_delete=models.CASCADE,
        related_name='answers'
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers'
    )

    selected_choice = models.ForeignKey(
        Choice,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='selected_answers'
    )

    is_correct = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['attempt', 'question'],
                name='unique_question_per_attempt'
            )
        ]

    def __str__(self):
        return f"{self.attempt.student.username} - {self.question}"