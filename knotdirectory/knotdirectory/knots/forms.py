from django import forms
from django.forms.models import inlineformset_factory
from django.utils import six

from .models import Knot, Link


def edit_string_for_tags(tags):
    """
    Convert list of Tags into comma-separated list.

    We can't use the one built into django-taggit, because select2 freaks out
    about the space after the comma.
    """
    names = []
    for tag in tags:
        name = tag.name
        if ',' in name or ' ' in name:
            names.append('"%s"' % name)
        else:
            names.append(name)
    return ','.join(sorted(names))


class HiddenTagWidget(forms.HiddenInput):
    """ For use with select2 and ajax tagging """
    def render(self, name, value, attrs=None):
        if value is not None and not isinstance(value, six.string_types):
            value = edit_string_for_tags([o.tag for o in value.select_related("tag")])
        return super(HiddenTagWidget, self).render(name, value, attrs)


class KnotForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(KnotForm, self).__init__(*args, **kwargs)
        print self.fields.keys()
        self.fields['tags'].widget = HiddenTagWidget()

    class Meta:
        model = Knot
        fields = ['name', 'photo', 'other_names', 'creator_name', 'notes', 'tags']


class InlineLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['name', 'link']

LinkFormset = inlineformset_factory(Knot, Link)
