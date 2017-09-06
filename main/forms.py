from django import forms
from django.forms import formset_factory


class TitleForm(forms.Form):
    title = forms.CharField(label='Songbook General Tite', required=False)


class SongBookForm(forms.Form):
    song = forms.CharField(label='Song', widget=forms.Textarea)


SongBookFormSet = formset_factory(SongBookForm, extra=5)
