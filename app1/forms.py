from django.forms import ModelForm
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django import forms



class roomcreate(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host','participants']




class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']      


# class loginpageform(forms.Form):
#     username=forms.CharField(max_length=200)
#     password=forms.CharField(widget=forms.PasswordInput)


# class uploadform(ModelForm):
#     class Meta:
#         model = upload
#         fields ='__all__'



class profileform(forms.Form):
   
  
 year=forms.ChoiceField(choices=[
      ('first','first'),
      ('Second','Second'),
      ('Third','Third'),
      ('Fourth','Fourth'),
     
   ])
 branch=forms.ChoiceField(choices=[
      ('CSE','CSE'),
      ('ISE','ISE'),
      ('AI-ML','AI-ML'),
      ('ECE','ECE'),
      ('EEE','EEE'),
      ('MECHE','MECH'),
    
   ])
 
 photo = forms.FileField()
 interests=forms.CharField(max_length=200)
 bio=forms.CharField(max_length=200)
            
        



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'year','branch','interests', 'bio']        