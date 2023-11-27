from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from todo.models import Task, Tag


def validate_deadline(deadline):
    datetime_now = timezone.now()
    if deadline <= datetime_now:
        raise ValidationError(
            "Oops! This deadline is not realistic. Try picking another time."
        )
    return deadline


class TaskCreationForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        help_text="Select one or more",
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        help_text="year-moth-day 00:00:00",
        widget=forms.DateTimeInput(attrs={"class": "datetime-input"}),
        input_formats=["%Y-%m-%d %H:%M:%S"],
        validators=[validate_deadline],
        required=False,
    )

    class Meta:
        model = Task
        fields = "__all__"


class TagCreationForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
