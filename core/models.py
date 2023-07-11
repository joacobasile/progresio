# from django.contrib.auth import get_user_model
from django.db import models
from users.models import CustomUser


# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True)

    STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('Started', 'Started'),
        ('In progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, default=start_date)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')

    def __str__(self):
        return self.title
