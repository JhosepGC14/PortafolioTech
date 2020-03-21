from django import forms
from.models import Job

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('summary', 'title','image')