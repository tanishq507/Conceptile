from django.urls import path
from .views import (
    StartQuizView,
    GetQuestionView,
    SubmitAnswerView,
    QuizStatsView
)

urlpatterns = [
    path('quiz/start/', StartQuizView.as_view(), name='start-quiz'),
    path('quiz/question/', GetQuestionView.as_view(), name='get-question'),
    path('quiz/submit/', SubmitAnswerView.as_view(), name='submit-answer'),
    path('quiz/stats/', QuizStatsView.as_view(), name='quiz-stats'),
]