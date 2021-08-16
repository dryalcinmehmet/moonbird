from django.contrib import admin
from .models import Osos


class OsosAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Osos._meta.get_fields()]


admin.site.register(Osos, OsosAdmin)
# Register your models here.
