from datetime import date
from django import forms

class AddHabit(forms.Form):
    name = forms.CharField(max_length=100, help_text="Enter a name for this habit.")
    goal = forms.IntegerField(min_value=0, help_text="Enter an integer representing your daily goal for this habit.")


class AddRecord(forms.Form):
    date = forms.DateField(initial=date.today, required=True)
    actual = forms.IntegerField(min_value=0, help_text="Enter your actual data from the day.", required=True)

class this(forms.Form):
    actual = forms.IntegerField(min_value=0)