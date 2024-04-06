from django import forms
from .models import Course

class Order(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(),widget=forms.Select(attrs={'class':'form-control s'}))