from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок', widget=forms.Textarea())
    text = forms.CharField(label='Содержание', widget=forms.Textarea())
    class Meta:
        model = Post
        fields = ('title', 'text',)