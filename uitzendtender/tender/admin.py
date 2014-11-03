from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
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


class TenderUserAdmin(UserAdmin):
    add_form = TenderUserCreationForm
    form = TenderUserChangeForm

    list_display = ("email", "is_staff", "userrole",)
    list_filter = ("is_staff", "is_superuser", "is_active", "groups", "userrole",)
    search_fields = ("email", "userrole",)
    ordering = ("userrole", "email",)
    filter_horizontal = ("groups", "user_permissions",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Role", {"fields": ("userrole",)}),
        ("Permissions", {"fields": ("is_active",
                            "is_staff",
                            "is_superuser",
                            "groups",
                            "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "userrole", "password1", "password2")}
        ),
    )

admin.site.register(TenderUser, TenderUserAdmin)

