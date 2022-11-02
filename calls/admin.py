import imp
from django.contrib import admin

# Register your models here.

from .models import calls
from .models import callStatus

admin.site.register(calls)


# Register your models here.
# class YourModelAdmin(admin.ModelAdmin):
#     fields = ('call_type_choices', )

admin.site.register(callStatus)
