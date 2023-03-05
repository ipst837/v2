from django.contrib import admin
from .models import GamesList


class ListAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(GamesList, ListAdmin)
