from django import forms
from .models import Contact
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'username':TextInput(attrs={'placeholder':"الاسم",'class':"required form-control",}),
            'email':EmailInput(attrs={'placeholder':"بريد الالكتروني",'class':"required form-control",}),
            'phone':TextInput(attrs={'placeholder':"رقم التليفون",'class':"required form-control" ,}),
            'message':Textarea(attrs={'placeholder':"رسالة",'class':"required form-control"}),
         }