from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from models import Entry

class EntryDetail(DetailView):
    context_object_name = 'entry'
    template_name = 'happy_blog/entry_detail.html'

    def get_queryset(self):
        return Entry.all_published.language().filter(pub_date__year=self.kwargs['year'], pub_date__month=self.kwargs['month'], pub_date__day=self.kwargs['day'])