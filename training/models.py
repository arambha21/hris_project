from django.db import models
from employees.models import Employee

class TrainingSession(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    trainer = models.CharField(max_length=100)
    max_participants = models.PositiveIntegerField()
    participants = models.ManyToManyField(Employee, related_name='training_sessions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
