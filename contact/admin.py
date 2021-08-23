from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created']
    list_filter = ['created']
    search_fields = ['name', 'subject', 'message', 'email', 'phone']
