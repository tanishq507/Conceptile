from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .services import QuizService
from .serializers import (
    QuizSessionSerializer,
    QuestionSerializer,
    UserAnswerSerializer,
    QuizStatsSerializer
)

class StartQuizView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        session = QuizService.start_new_session(request.user)
        serializer = QuizSessionSerializer(session)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetQuestionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        active_session = request.user.quizsession_set.filter(is_active=True).first()
        if not active_session:
            return Response(
                {"error": "No active quiz session found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        question = QuizService.get_random_question(active_session)
        if not question:
            return Response(
                {"message": "No more questions available"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = QuestionSerializer(question)
        return Response(serializer.data)

class SubmitAnswerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        session = request.user.quizsession_set.filter(is_active=True).first()
        if not session:
            return Response(
                {"error": "No active quiz session found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        question_id = request.data.get('question_id')
        choice_id = request.data.get('choices_id')

        if not all([question_id, choice_id]):
            return Response(
                {"error": "Question ID and Choice ID are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            answer = QuizService.submit_answer(session, question_id, choice_id)
            serializer = UserAnswerSerializer(answer)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class QuizStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        session = request.user.quizsession_set.filter(is_active=True).first()
        if not session:
            return Response(
                {"error": "No active quiz session found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        stats = QuizService.get_session_stats(session)
        serializer = QuizStatsSerializer(stats)
        return Response(serializer.data)