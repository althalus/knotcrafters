from django import forms
from django.forms.models import inlineformset_factory

from .models import Knot, Link


class KnotForm(forms.ModelForm):
    class Meta:
        model = Knot
        fields = ['name', 'photo', 'other_names', 'creator_name', 'notes', 'tags']


class InlineLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['name', 'link']

LinkFormset = inlineformset_factory(Knot, Link)
