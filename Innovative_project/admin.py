from django.contrib import admin

from Innovative_project.models import User, Host


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "phone",
        "host",
    )


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "hostname",
        "address",
        "phone",
        "email",
    )
