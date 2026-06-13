from django import forms
from django.utils import timezone

from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'position', 'hire_date', 'salary', 'email']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'hire_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'min': '0.01', 'step': '0.01'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name', '').strip()
        if not full_name:
            raise forms.ValidationError('ФИО не может быть пустым.')
        return full_name

    def clean_position(self):
        position = self.cleaned_data.get('position', '').strip()
        if not position:
            raise forms.ValidationError('Должность не может быть пустой.')
        return position

    def clean_hire_date(self):
        hire_date = self.cleaned_data.get('hire_date')
        if hire_date and hire_date > timezone.now().date():
            raise forms.ValidationError('Дата приёма не может быть в будущем.')
        return hire_date

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary is not None and salary <= 0:
            raise forms.ValidationError('Зарплата должна быть больше нуля.')
        return salary

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip()
        if email and '@' not in email:
            raise forms.ValidationError('Email должен содержать символ @.')
        qs = Employee.objects.filter(email=email)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Сотрудник с таким email уже существует.')
        return email
