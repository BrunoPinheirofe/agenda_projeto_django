from tkinter import Widget
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from contact.models import Contact
from django.contrib.auth import password_validation


class ContactForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "classe-a", "placeholder": "Nome"}),
        label="Primeiro Nome",
        help_text="Ex: Bruno",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields["first_name"].widget.attrs.update(
        #
        # )

    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "description",
            "category",
        )
        # widgets = {
        #     'first_name': forms.TextInput(

        #         attrs={
        #             'class':'classe-a',
        #             'placeholder': 'Nome',

        #         }
        #     )
        # }

    def clean(self):

        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        msg = ValidationError("O primeiro nome não pode ser igual ao segundo nome")
        cleaned_data = self.cleaned_data

        if first_name == last_name:
            self.add_error("first_name", msg)
            self.add_error("last_name", msg)

        return super().clean()

    def clean_first_name(self):
        data: str = self.cleaned_data.get("first_name")
        if not data.isalpha():
            self.add_error(
                "first_name", ValidationError("Veio do add error", code="invalid")
            )

        return data


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    def cleaned_email(self):
        email = self.cleaned_email["email"]

        if User.objects.filter(email=email).exists():
            self.add_error(
                "email", ValidationError("Email já cadastrado", code="invalid")
            )

        return email


class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text={"min_length": "Please, add more than 2 letters"},
    )
    last_name = forms.CharField(
        min_length=2, max_length=30, required=True, help_text="Required"
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
        )

        def save(self, commit=True):
            cleaned_data = self.cleaned_data
            user = super().save(commit=False)
            password = cleaned_data.get("password1")

            if password:
                user.set_password(password)

            if commit:
                user.save()
            return user

        def clean(self):
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")

            if password1 or password2:
                if password1 != password2:
                    self.add_error(
                        "password2", ValidationError("senhas não são iguais")
                    )

            return super().clean()

        def clean_email(self):
            email = self.cleaned_data.get("email")
            current_email = self.instance.email
            if current_email != email:
                if User.objects.filter(email=email).exists():
                    self.add_error(
                        "email",
                        ValidationError("Já existe este e-mail", code="invalid"),
                    )

            return email

        def clean_password1(self):
            password1 = self.cleaned_data.get("password1")
            if password1:
                try:
                    password_validation.validate_password(password1)
                except ValidationError as errors:
                    self.add_error("password1", ValidationError(errors))
            return password1
