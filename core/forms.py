from django import forms
from .models import Habit, Record


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            "user",
            "name",
        ]


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [
            "habit",
            "date_completed",
        ]