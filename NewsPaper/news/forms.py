from django import forms
from .models import Post, Category
from django.forms import CharField, ModelMultipleChoiceField


class PostForm(forms.ModelForm):
    category = ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        label='Категория',
    )
    title = CharField(
        min_length=4,
        label='Заголовок',
    )

    class Meta:
        model = Post
        fields = [
            'category',
            'title',
            'text',
        ]
