from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class UpdatePasswordForm(forms.Form):
    current = forms.CharField(label='Current password',
                              widget=forms.PasswordInput)

    password1 = forms.CharField(label='New password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation',
        help_text='Same password as above.',
        widget=forms.PasswordInput,
    )
    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        assert self.instance is not None
        super(UpdatePasswordForm, self).__init__(*args, **kwargs)

    def clean_current(self):
        password = self.cleaned_data['current']

        assert self.instance is not None
        if not self.instance.check_password(password):
            raise forms.ValidationError("The current password was invalid.")

        return password

    def clean(self):
        cleaned_data = super(UpdatePasswordForm, self).clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise forms.ValidationError("Passwords didn't match")
        return cleaned_data

    def save(self, commit=True):
        assert self.instance is not None
        self.instance.set_password(self.cleaned_data['password1'])
        if commit:
            self.instance.save()
        return self.instance
