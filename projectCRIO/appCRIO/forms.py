from django import forms
from appCRIO.models import Meme

class MemeForm(forms.ModelForm):
    class Meta():
        model=Meme
        fields=('mid','name','meme_url')
