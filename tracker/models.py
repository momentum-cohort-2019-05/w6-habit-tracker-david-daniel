from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Habit(models.Model):
    name = models.CharField(max_length=100, help_text="Enter a name for ")
    date = models.DateField(auto_now_add=True)
    goal = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('habit-detail', args=[str(self.pk)])

    def __str__(self):
        return f'{self.name}'

class Record(models.Model):
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    actual = models.IntegerField()
    
    def __str__(self):
        return f'{self.date}'

    
    class Meta:
        ordering = ['-date']
        unique_together = ['habit', 'date']
