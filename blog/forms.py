from django import forms
from .models import MyUser

class UseForm(forms.ModelForm):
     
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter password: ',
            'id': 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter password confirmation: ',
            'id': 'password2',
            'required': 'required',
        }
    ))
    
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'image', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user
