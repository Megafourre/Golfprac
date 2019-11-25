from django import forms
from .models import Scorecard

class ScorecardForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('played_date', 'location','hole','score')
