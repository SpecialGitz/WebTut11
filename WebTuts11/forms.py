from django import forms

class ImageUploadForm(forms.Form):
    name = forms.CharField()
    image = forms.ImageField()