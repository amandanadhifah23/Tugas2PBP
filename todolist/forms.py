from django import forms

class FormTask(forms.Form):
   title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'Create New Task'}))
   description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'placeholder': 'Description'}))
