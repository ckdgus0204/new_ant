from django.contrib import admin
from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'username',
        'name',
    )

    list_display_links = (
        'username',
        'name',
    )