from django.contrib import admin

# Register your models here.
from pets.models import Pet, Like


class Pets(admin.ModelAdmin):
    list_display = ['type', 'name', 'age', ]
    list_filter = ['type', 'name', 'age']

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Pet)
admin.site.register(Like)
