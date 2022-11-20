from django import forms
from .models import Todo

class TaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = {'task_name'}

        widgets = {
            'task_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add a new task'
            })
        }