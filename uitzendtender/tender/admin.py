from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import TenderUser
from .forms import TenderUserCreationForm, TenderUserChangeForm



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

