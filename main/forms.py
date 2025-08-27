from django import forms

from .models import Habit, Category

class HabitUpdateForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description', 'category',]

class HabitCreationForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description', 'category',]

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'color']


