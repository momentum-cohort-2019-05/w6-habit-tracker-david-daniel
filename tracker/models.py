from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Habit(models.Model):
    name = models.CharField(max_length=100, help_text="Enter a name for ")
    date = models.DateField(auto_now_add=True)
    goal = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Record(models.Model):
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    actual = models.IntegerField()
    
    def __str__(self):
        return f'{self.date}'

    
    class Meta:
        ordering = ['-date']
