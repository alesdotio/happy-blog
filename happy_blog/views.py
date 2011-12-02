from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from models import Entry

class EntryDetail(DetailView):
    context_object_name = 'entry'
    template_name = 'happy_blog/entry_detail.html'

    def get_queryset(self):
        return Entry.all_published.filter(pub_date__year=self.kwargs['year'], pub_date__month=self.kwargs['month'], pub_date__day=self.kwargs['day'])

class BlogArchive(ListView):
    context_object_name = 'entries'
    queryset = Entry.all_published.order_by('pub_date')
    template_name = 'happy_blog/archive.html'

class BlogFeed(Feed):
    title_template = 'happy_blog/feed_title.html'
    description_template = 'happy_blog/feed_description.html'

    def link(self, obj):
        return reverse('happy_blog_archive')

    def get_queryset(self, obj):
        return Entry.all_published.order_by('pub_date')

    def items(self, obj):
        return self.get_queryset(obj)[:10]