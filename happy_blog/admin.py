from django.contrib import admin
from nani.admin import TranslatableAdmin
from models import Entry

class EntryAdmin(TranslatableAdmin):
    list_display = ('__unicode__', 'pub_date', 'is_published')

admin.site.register(Entry, EntryAdmin)