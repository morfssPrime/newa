from .models import AlumniAchievement
from django.forms import ModelForm, TextInput, Textarea


class AlumniAchievementForm(ModelForm):
    class Meta:
        model = AlumniAchievement
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите данные'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите достижения'
            }),
        }