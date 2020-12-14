from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.TextField()
    complete = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.task