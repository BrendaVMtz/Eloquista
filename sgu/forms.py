from django import forms
from .models import Teacher, Parent, User

class UserSignUpForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'type': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'email','password')
        widgets = {
            'is_teacher': forms.HiddenInput(),
            'is_parent': forms.HiddenInput()
        }

class TeacherSignUpForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('institution', 'phoneNumber')

class ParentSignUpForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ('street', 'number', 'city', 'phoneNumber')
