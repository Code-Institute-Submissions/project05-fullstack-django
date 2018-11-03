from django import forms
from .models import Bug, Feature


class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('title', 'details', 'image', 'tag', 'published_date')


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('title', 'details', 'tag', 'published_date')
