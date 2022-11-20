from django.db import models

# Create your models here.
class Todo(models.Model):
    task_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)