from django.db import models
from .Module import Module

class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField()
    duration_in_minutes = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'courses'
        ordering = ['order']
    def __str__(self):
        return f"{self.module.course.title} - {self.module.title} - {self.title}"