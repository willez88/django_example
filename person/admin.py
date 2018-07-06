from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('user','first_name','last_name','identification_card',)
    list_filter = ('user',)
    list_per_page = 25
    ordering = ('user',)
admin.site.register(Person, PersonAdmin)
