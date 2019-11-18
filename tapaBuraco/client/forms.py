from django import forms

class Form(forms.Form):
    latitude = forms.CharField(label='Latitude', max_length=100)
    longitude = forms.CharField(label='Longitude', max_length=100)
    aceleracao = forms.CharField(label='Aceleração', max_length=100)