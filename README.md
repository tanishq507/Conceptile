# Quiz Application

A Django REST API-based quiz application that allows users to take quizzes, submit answers, and track their progress.

## Features

- User authentication
- Start new quiz sessions
- Get random multiple-choice questions
- Submit answers
- Track quiz statistics
- Admin interface for managing questions and choices

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd quiz-project
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Load sample questions:
```bash
python manage.py add_sample_questions
```

7. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication

Access the admin interface at `http://localhost:8000/admin/` to log in.

### Quiz Endpoints

All endpoints require authentication.

1. **Start New Quiz Session**
   - URL: `/api/quiz/start/`
   - Method: POST
   - Response:
     ```json
     {
         "id": 1,
         "started_at": "2024-01-20T10:00:00Z",
         "is_active": true
     }
     ```

2. **Get Random Question**
   - URL: `/api/quiz/question/`
   - Method: GET
   - Response:
     ```json
     {
         "id": 1,
         "text": "What does HTML stand for?",
         "choices": [
             {
                 "id": 1,
                 "text": "Hyper Text Markup Language"
             },
             {
                 "id": 2,
                 "text": "High Tech Modern Language"
             }
         ]
     }
     ```

3. **Submit Answer**
   - URL: `/api/quiz/submit/`
   - Method: POST
   - Request Body:
     ```json
     {
         "question_id": 1,
         "choices_id": 1
     }
     ```
   - Response:
     ```json
     {
         "id": 1,
         "question": 1,
         "selected_choice": 1,
         "is_correct": true,
         "answered_at": "2024-01-20T10:05:00Z"
     }
     ```

4. **Get Quiz Statistics**
   - URL: `/api/quiz/stats/`
   - Method: GET
   - Response:
     ```json
     {
         "total_questions": 5,
         "correct_answers": 3,
         "incorrect_answers": 2,
         "accuracy": 60.0
     }
     ```

## Sample Questions

The application comes with 5 sample questions covering different topics:
1. HTML definition
2. Chemical symbol for gold
3. Value of π (pi)
4. Largest ocean on Earth
5. End of World War II

You can add more questions through the admin interface or by modifying the `add_sample_questions.py` management command.






