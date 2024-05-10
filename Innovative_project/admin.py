from django.contrib import admin
from Innovative_project.users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'host_id')  # Fields to display in list view


admin.site.register(User, UserAdmin)
# Register your models here.
