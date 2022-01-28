from django.forms import ModelForm
from .models import task

class taskForm(ModelForm):
    class Meta:
        model = task
        fields = '__all__'
        labels ={
            'host': 'User',
            'task': 'Task',
            'desc': 'Description'
        }

    def __init__(self, *args, **kwargs):
        super(taskForm, self).__init__(*args, **kwargs)
        self.fields['host'].empty_label = "click here to select the user"