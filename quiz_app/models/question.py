from django.db import models
from ..utils.validators import validate_question_choices

class Question(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
        
    def clean(self):
        """Validate the question has valid choices"""
        if self.id:  # Only validate if question already exists
            validate_question_choices(self)
        super().clean()

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text