from django.db.models import Count, Q

from quiz_app.models import Choice
from ..models import Question, QuizSession, UserAnswer
from ..utils.session_utils import deactivate_old_sessions, is_session_expired
import random

class QuizService:
    @staticmethod
    def start_new_session(user):
        """Create a new quiz session for the user"""
        # Deactivate any existing active sessions
        deactivate_old_sessions(user)
        return QuizSession.objects.create(user=user)

    @staticmethod
    def get_random_question(session):
        """Get a random question that hasn't been answered in the current session"""
        if is_session_expired(session):
            session.is_active = False
            session.save()
            return None
            
        answered_questions = UserAnswer.objects.filter(
            session=session
        ).values_list('question_id', flat=True)
        
        available_questions = Question.objects.exclude(
            id__in=answered_questions
        )
        
        if not available_questions.exists():
            return None
            
        return random.choice(available_questions)

    @staticmethod
    def submit_answer(session, question_id, choice_id):
        """Submit an answer for the current question"""
        if is_session_expired(session):
            session.is_active = False
            session.save()
            raise ValueError("Quiz session has expired")
            
        choice = Choice.objects.get(id=choice_id)
        
        # Verify this question hasn't been answered in this session
        if UserAnswer.objects.filter(session=session, question_id=question_id).exists():
            raise ValueError("Question has already been answered in this session")
        
        return UserAnswer.objects.create(
            session=session,
            question_id=question_id,
            selected_choice=choice,
            is_correct=choice.is_correct
        )

    @staticmethod
    def get_session_stats(session):
        """Get statistics for the current session"""
        answers = UserAnswer.objects.filter(session=session)
        total = answers.count()
        correct = answers.filter(is_correct=True).count()
        
        return {
            'total_questions': total,
            'correct_answers': correct,
            'incorrect_answers': total - correct,
            'accuracy': (correct / total * 100) if total > 0 else 0
        }