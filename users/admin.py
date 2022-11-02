import imp
from django.contrib import admin
from .models import NewUser

# Register your models here.
# class YourModelAdmin(admin.ModelAdmin):
#     fields = ('role_type', 'store_type' )

# admin.site.register(NewUser, YourModelAdmin)





from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    # fields = ('role_type', 'store_type' )
    model = NewUser
    search_fields = ('email', 'user_name',)
    list_filter = ('email', 'user_name', 'contact','store_type' ,'is_active', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name','contact','store_type',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name','role_type', 'store_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'contact', 'password1', 'password2','role_type' ,'store_type' ,'is_active', 'is_staff')}
         ),
    )



admin.site.register(NewUser, UserAdminConfig)