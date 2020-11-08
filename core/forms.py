from django import forms
from .models import Habit, Record


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            "name",
        ]


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [
            "record_response",
            "date_completed",
        ]


class SearchForm(forms.Form):
    name = forms.CharField(max_length=255)