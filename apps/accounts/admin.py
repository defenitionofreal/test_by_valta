from django.contrib import admin
from apps.accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("id", "email")
    list_display = ("id", "email", "is_superuser")
