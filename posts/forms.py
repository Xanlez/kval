from django import forms
from django.utils import timezone

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published_at', 'views', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'published_at': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d',
            ),
            'views': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if not title:
            raise forms.ValidationError('Заголовок не может быть пустым.')
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise forms.ValidationError('Содержание не может быть пустым.')
        return content

    def clean_published_at(self):
        published_at = self.cleaned_data.get('published_at')
        if published_at and published_at > timezone.localdate():
            raise forms.ValidationError('Дата публикации не может быть в будущем.')
        return published_at

    def clean_views(self):
        views = self.cleaned_data.get('views')
        if views is not None and views < 0:
            raise forms.ValidationError('Количество просмотров не может быть отрицательным.')
        return views
