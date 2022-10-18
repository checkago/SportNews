from django import forms
from web.models import *
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()
    body = forms.CharField(
        label='Текст комментария',
        widget=forms.Textarea(attrs={'rows': '5'})
    )


    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')