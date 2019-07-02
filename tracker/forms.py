from django import forms

class edit_record(forms.Form):
    actual = forms.IntegerField(min_value=0)