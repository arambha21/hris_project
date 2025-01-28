from django.db import models
from employees.models import Employee

class PerformanceReview(models.Model):
    RATING_CHOICES = [
        (1, 'Poor'),
        (2, 'Below Average'),
        (3, 'Average'),
        (4, 'Above Average'),
        (5, 'Excellent'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performance_reviews_performance')
    reviewer = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reviews_given_performance')
    review_date = models.DateField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    comments = models.TextField()
    goals = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review for {self.employee} on {self.review_date}"
