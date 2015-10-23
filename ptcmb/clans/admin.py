from django.contrib import admin

from .models import Clan_Meta_Data

class Clan_Meta_Data_Admin(admin.ModelAdmin):
    fieldsets = [
    ('Info', {'fields': ['name']}),
    ('Stats', {'fields': ['coins', 'posts', 'comments']}),
    ]

admin.site.register(Clan_Meta_Data, Clan_Meta_Data_Admin)
# Register your models here.
