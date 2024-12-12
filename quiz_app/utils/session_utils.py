from django.utils import timezone

def is_session_expired(session, max_duration_minutes=30):
    """Check if a quiz session has expired based on duration"""
    if not session.is_active:
        return True
        
    duration = timezone.now() - session.started_at
    return duration.total_seconds() / 60 > max_duration_minutes

def deactivate_old_sessions(user):
    """Deactivate any active sessions for the user"""
    user.quizsession_set.filter(is_active=True).update(is_active=False)