from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import TenderUser


class TenderUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Wachtwoord",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Bevestig wacthwoord",
                                widget=forms.PasswordInput)

    class Meta:
        model = TenderUser
        fields = ("email", "userrole")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            msg = "Wachtwoorden komen niet met elkaar overeen."
            raise forms.ValidationError(msg)
        return password2

    def save(self, commit=True):
        user = super(TenderUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class TenderUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = TenderUser

    def clean_password(self):
        return self.initial["password"]