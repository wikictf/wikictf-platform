from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from crispy_forms.layout import Submit
from django.core.exceptions import ValidationError
class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=200,
        required=True

    )
    password = forms.CharField(widget=forms.PasswordInput,
                               label="Password")

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'loginForm'
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.helper.add_input(Submit('submit', 'Login'))

class SignupForm(forms.Form):
    username = forms.CharField(
        label = "Username",
        max_length = 200,
        required=True

    )
    email = forms.EmailField(
        label="Email",
        max_length=200,
        required=True

    )
    password = forms.CharField(widget=forms.PasswordInput,
                               label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label="Password (Again)")

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'signupForm'
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise ValidationError('Username already exists.')
        if cleaned_data.get('password') != cleaned_data.get('password2'):
            raise ValidationError('Passwords do not match')

        return cleaned_data