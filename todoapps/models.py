from django.db import models

class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of a model"""
        return self.text

class Task(models.Model):
    """A task part of a topic"""
    task = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'tasks'

    def __str__(self):
        """Return a string representation of the model"""
        return self.text
