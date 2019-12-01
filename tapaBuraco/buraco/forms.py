from django import forms

class Form(forms.Form):
	latitude = forms.DecimalField(max_digits=20, decimal_places=7, label='Latitude')
	longitude = forms.DecimalField(max_digits=20, decimal_places=7,label='Longitude')
	acc =  forms.FloatField(label='Aceleração')

class LoginForm(forms.Form):
	email = forms.EmailField()
	senha = forms.CharField()