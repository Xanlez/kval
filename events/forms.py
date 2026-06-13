from django import forms
from django.utils import timezone

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'location', 'event_date', 'max_guests']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'event_date': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M',
            ),
            'max_guests': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['event_date'].input_formats = ['%Y-%m-%dT%H:%M', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M']

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if not title:
            raise forms.ValidationError('Название не может быть пустым.')
        return title

    def clean_event_date(self):
        event_date = self.cleaned_data.get('event_date')
        if event_date and event_date <= timezone.now():
            raise forms.ValidationError('Дата мероприятия должна быть в будущем.')
        return event_date

    def clean_max_guests(self):
        max_guests = self.cleaned_data.get('max_guests')
        if max_guests is not None and max_guests <= 0:
            raise forms.ValidationError('Максимальное число гостей должно быть больше нуля.')
        return max_guests
