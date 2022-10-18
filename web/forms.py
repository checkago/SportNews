from django import forms
from web.models import *


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        label='Текст комментария',
        widget=forms.Textarea(attrs={'rows': '5'})
    )

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')