from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact


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
            'email',
            'description',
            'category'
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
            self.add_error('first_name',msg)
            self.add_error('last_name',msg)

        return super().clean()

    def clean_first_name(self):
        data: str = self.cleaned_data.get("first_name")
        if not data.isalpha():
            self.add_error(
                "first_name", ValidationError("Veio do add error", code="invalid")
            )

        return data
