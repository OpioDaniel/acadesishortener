from django import forms
from .validators import validate_url, validate_dot_com


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Enter the Link here',  validators=[validate_url, validate_dot_com])

