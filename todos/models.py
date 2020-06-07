from django.db import models
import datetime


class Todo(models.Model):
    todo = models.CharField(max_length=100)
    isFinished = models.BooleanField(default=False)
    untilWhen = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        ordering = ['untilWhen']

    def __str__(self):
        return self.todo
