from django.db import models
from .User import User
from .Instructor import Instructor
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')
    level =  models.CharField(max_length=50, default='beginner')
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'courses'
    def __str__(self):
        return self.title