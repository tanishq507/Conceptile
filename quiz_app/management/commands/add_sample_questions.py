from django.core.management.base import BaseCommand
from quiz_app.models import Question, Choice

class Command(BaseCommand):
    help = 'Adds sample questions and choices to the database'

    def handle(self, *args, **kwargs):
        # Question 1: Programming
        q1 = Question.objects.create(text="What does HTML stand for?")
        Choice.objects.create(question=q1, text="Hyper Text Markup Language", is_correct=True)
        Choice.objects.create(question=q1, text="High Tech Modern Language", is_correct=False)
        Choice.objects.create(question=q1, text="Hyperlinks and Text Markup Language", is_correct=False)
        Choice.objects.create(question=q1, text="Home Tool Markup Language", is_correct=False)

        # Question 2: Science
        q2 = Question.objects.create(text="What is the chemical symbol for gold?")
        Choice.objects.create(question=q2, text="Au", is_correct=True)
        Choice.objects.create(question=q2, text="Ag", is_correct=False)
        Choice.objects.create(question=q2, text="Fe", is_correct=False)
        Choice.objects.create(question=q2, text="Cu", is_correct=False)

        # Question 3: Mathematics
        q3 = Question.objects.create(text="What is the value of π (pi) to two decimal places?")
        Choice.objects.create(question=q3, text="3.14", is_correct=True)
        Choice.objects.create(question=q3, text="3.16", is_correct=False)
        Choice.objects.create(question=q3, text="3.12", is_correct=False)
        Choice.objects.create(question=q3, text="3.18", is_correct=False)

        # Question 4: Geography
        q4 = Question.objects.create(text="Which is the largest ocean on Earth?")
        Choice.objects.create(question=q4, text="Pacific Ocean", is_correct=True)
        Choice.objects.create(question=q4, text="Atlantic Ocean", is_correct=False)
        Choice.objects.create(question=q4, text="Indian Ocean", is_correct=False)
        Choice.objects.create(question=q4, text="Arctic Ocean", is_correct=False)

        # Question 5: History
        q5 = Question.objects.create(text="In which year did World War II end?")
        Choice.objects.create(question=q5, text="1945", is_correct=True)
        Choice.objects.create(question=q5, text="1944", is_correct=False)
        Choice.objects.create(question=q5, text="1946", is_correct=False)
        Choice.objects.create(question=q5, text="1943", is_correct=False)

        self.stdout.write(self.style.SUCCESS('Successfully added sample questions and choices'))