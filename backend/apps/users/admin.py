from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


# register new rows for admin
UserAdmin.list_display += ('info', )
UserAdmin.fieldsets += (
    ('Info', {
        'fields': ('info', )
    }),
)

admin.site.register(User, UserAdmin)
