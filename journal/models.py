from django.db import models
from django.contrib.auth.models import User

class JournalEntry(models.Model):
    MOOD_CHOICES = [
        ('happy', '😊 Happy'),
        ('sad', '😢 Sad'),
        ('angry', '😠 Angry'),
        ("frustrated", "😤 Frustrated"),
        ('neutral', '😐 Neutral'),
        ('excited', '🤩 Excited'),
        ('anxious', '😰 Anxious'),
        ('confused', '😵‍💫 Confused'),
        ('calm', '😌 Calm'),
        ('tired', '🥱 Tired'),
        ('stressed', '😖 Stressed')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES, default='neutral')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.get_mood_display()})"
