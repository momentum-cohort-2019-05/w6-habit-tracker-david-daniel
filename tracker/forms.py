from django import forms

class edit_record(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)