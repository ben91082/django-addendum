# encoding: utf-8

from django import forms
from django.conf import settings

from .models import SnippetTranslation, Snippet
from tinymce.widgets import TinyMCE


class SnippetForm(forms.ModelForm):

    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Snippet
        fields = "__all__"

class TranslationForm(forms.ModelForm):

    language = forms.ChoiceField(choices=settings.LANGUAGES, initial="en")

    class Meta:
        model = SnippetTranslation
        fields = "__all__"
