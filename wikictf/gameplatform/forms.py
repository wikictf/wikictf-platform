from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
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
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'signupForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submitSignup'
        self.helper.add_input(Submit('submit', 'Submit'))