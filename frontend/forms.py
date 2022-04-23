from django.forms import ModelForm
from api.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'body')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'placeholder': 'Enter title'})
        self.fields['body'].widget.attrs.update({'placeholder': 'Enter body'})

        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})