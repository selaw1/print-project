from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

@admin.register(get_user_model())
class AccountAdmin(BaseUserAdmin):

    fieldsets = (
        ('Account Information', {"fields": ('email', 'username', 'password', 'first_name','last_name','slug')}),
        ('Permissions', {"fields": ('is_active', 'is_staff', 'is_superuser', 'is_print_factory_boss', 'groups', 'user_permissions'), "classes": ('collapse',)}),
        ('Important dates', {'fields': ('last_login',), "classes": ('collapse',)})
    )

    list_display = ('username', 'email', 'slug', 'id', 'is_staff', 'is_active', 'last_login' )
    list_filter = ['is_active', 'is_staff', 'groups']
    search_fields = ['email', 'username', 'id', 'slug']
