from django.db import models

# Create your models here.
class Video(models.Model):
    url= " https://www.youtube.com/live/toIzHLO7rAI?si=2vK4L2lmRGurvRKf"
    added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.title)
    class Meta:
        ordering = ['added']
        