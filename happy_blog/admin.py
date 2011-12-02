from cms.admin.placeholderadmin import PlaceholderAdmin
from django.contrib import admin
from nani.admin import TranslatableAdmin
from models import Entry

class EntryAdmin(TranslatableAdmin, PlaceholderAdmin):
    list_display = ('__unicode__', 'pub_date', 'is_published')

admin.site.register(Entry, EntryAdmin)