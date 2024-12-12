from django.db import models
from django.contrib.auth.models import User
from .question import Question, Choice

class QuizSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Session {self.id} - {self.user.username}"

class UserAnswer(models.Model):
    session = models.ForeignKey(QuizSession, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    answered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.session.user.username}'s answer to {self.question.text}"
        
    class Meta:
        ordering = ['answered_at']