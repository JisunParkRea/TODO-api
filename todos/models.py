from django.db import models


class Todo(models.Model):
    todo = models.CharField(max_length=100)
    isFinished = models.BooleanField(default=False)
    untilWhen = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['untilWhen']

    def __str__(self):
        return self.todo
