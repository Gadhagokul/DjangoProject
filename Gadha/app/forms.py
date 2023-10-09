from django import forms
from .models import user1
 
class student(forms.ModelForm):
    class Meta:
        model=user1
        fields=['name','email','phone','password']
        widgets={'name':forms.TextInput(attrs={'placeholder':'Enter your name','style':'margin-left:55px;padding-left:15px','class':'form_control'}),
                'email':forms.TextInput(attrs={'placeholder':'Enter your email','style':'margin-left:60px;padding-left:15px','class':'form_control'}),
                'phone':forms.TextInput(attrs={'placeholder':'Enter your phone','style':'margin-left:50px;padding-left:15px','class':'form_control'}),
                'password':forms.PasswordInput(attrs={'placeholder':'Enter your password','style':'margin-left:20px;padding-left:15px','class':'form_control'}),}