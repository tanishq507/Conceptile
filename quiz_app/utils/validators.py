from django.core.exceptions import ValidationError

def validate_question_choices(question):
    """Validate that a question has at least 2 choices and exactly one correct answer"""
    choices = question.choices.all()
    
    if len(choices) < 2:
        raise ValidationError("Question must have at least 2 choices")
        
    correct_choices = sum(1 for choice in choices if choice.is_correct)
    if correct_choices != 1:
        raise ValidationError("Question must have exactly one correct choice")