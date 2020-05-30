from django import forms
from .models import Task, Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ('owner',)


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('user')
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(owner=current_user)
