from django import forms
from .models import Vote

class VoteForms(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ["fullname", "candidate_id"]
        labels = {
            "fullname": "نام و نام خانوادگی",
            "candidate_id": "کاندید مورد نظر"
        }
