from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from nani.models import TranslatableModel, TranslatedFields
from nani.manager import TranslationManager
import datetime
from time import strftime
from tinymce.models import HTMLField
from simplegallery.models import Gallery
from django.core.urlresolvers import reverse

class PublishedEntriesManager(TranslationManager):

    def get_query_set(self):
        return super(PublishedEntriesManager, self).language().filter(published=True, pub_date__lt=datetime.datetime.now())

class Entry(TranslatableModel):
    translatable = TranslatedFields(
        title = models.CharField(max_length=256, verbose_name=_('title')),
        slug = models.CharField(max_length=256, verbose_name=_('slug'), help_text=_('Title of the entry without spaces or special characters (only - is allowed). Has to be unique for the current date.')),
        content = HTMLField(blank=True, verbose_name=_('content')),
    )
    pub_date = models.DateTimeField(default=datetime.datetime.now, verbose_name=_('publish on'))
    published = models.BooleanField(default=False, verbose_name=_('published'))
    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name=_('author'))

    gallery = models.ForeignKey(Gallery, blank=True, null=True)

    all_published = PublishedEntriesManager()

    def is_published(self):
        return self.published and self.pub_date < datetime.datetime.now()
    is_published.boolean = True

    def get_absolute_url(self):
        arguments = [self.pub_date.strftime('%Y'), self.pub_date.strftime('%m'), self.pub_date.strftime('%d'), self.lazy_translation_getter('slug', '')]
        return reverse('happy_blog_entry_detail', args=arguments)

    def get_next(self):
        next = Entry.all_published.filter(pub_date__gt=self.pub_date)[:1]
        if next:
            next = next[0]
        else:
            next = None
        return next

    def get_prev(self):
        return Entry.all_published.filter(pub_date__lt=self.pub_date).latest('pub_date')

    def get_next_absolute_url(self):
        next = self.get_next()
        if next:
            return next.get_absolute_url()
        return ''

    def get_prev_absolute_url(self):
        prev = self.get_prev()
        if prev:
            return prev.get_absolute_url()
        return ''

    def get_first_image(self):
        if self.gallery:
            images = self.gallery.images.all()
            if images:
                return images[0].image
        return None

    class Meta:
        verbose_name = _('entry')
        verbose_name_plural = _('entries')
        get_latest_by = 'pub_date'
        ordering = ['pub_date']

    def __unicode__(self):
        return self.lazy_translation_getter('title', 'untranslated')

class LatestBlogEntriesPlugin(CMSPlugin):
    count = models.IntegerField(default=25)

    def copy_relations(self, oldinstance):
        self.count = oldinstance.count

    def __unicode__(self):
        return u'%s' % self.count