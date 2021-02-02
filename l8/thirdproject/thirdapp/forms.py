from django import forms
from .models import WnModel

CHOICES=[('django','django'),
         ('js','js'),
         ('go','go')]
class WnForm(forms.ModelForm):
	options = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
	class Meta:
		model=WnModel
		fields=['name','options']