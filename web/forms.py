from django import forms
from .models import Contact
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'firstname':TextInput(attrs={'placeholder':"الاسم الأول",'class':"required form-control",'name':"firstname",}),
            'lastname':TextInput(attrs={'placeholder':"الكنية",'class':"required form-control" ,'name':"lastname"}),
            'email':EmailInput(attrs={'placeholder':"بريد الالكتروني",'class':"required form-control" ,'name':"email"}),
            'phone':TextInput(attrs={'placeholder':"رقم التليفون",'class':"required form-control" ,'name':"phone"}),
            'feedback':Textarea(attrs={'placeholder':"ردود الفعل",'class':"required form-control" ,'name':"feedback"}),
         }