from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'priority', 'status', 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S'),
        }
        labels = {
            'title' : 'Task Title',
            'description' : 'Task Description',
            'category' : 'Category',
            'priority' : 'Priority',
            'status' : 'Status',
            'deadline' : 'Deadline',
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        
        # self.fields['category'].widget = forms.Select()
        # self.fields['priority'].widget = forms.Select()
        # self.fields['status'].widget = forms.Select()

        self.fields['deadline'].input_formats = ['%Y-%m-%dT%H:%M:%S']

    
