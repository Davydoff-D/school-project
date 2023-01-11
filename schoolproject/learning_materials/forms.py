from django import forms
from .models import Question, AnswerModel


class QuestionForm(forms.ModelForm):
    class Meta:
        model = AnswerModel
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={
                'cols': '25',
                'rows': '1',
                'class': 'form-control',
                'id': 'form_field',
                'type': 'text',
            }),
        }
