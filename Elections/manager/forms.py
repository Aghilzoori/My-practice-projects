from django import forms
from .models import Candidates

class CandidatesForms(forms.ModelForm):
    class Meta:
        model = Candidates
        fields = ["fullname"]
        labels = {"fullname": "نام و نام خانوادگی"}