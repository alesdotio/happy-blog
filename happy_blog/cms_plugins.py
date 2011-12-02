from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from models import Entry
from models import LatestBlogEntriesPlugin
from django.utils.translation import ugettext as _

class CMSLatestBlogEntriesPlugin(CMSPluginBase):
    model = LatestBlogEntriesPlugin
    name = _("Latest Blog Entries")
    render_template = "happy_blog/latest.html"
    entries = Entry.all_published.all()

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'entries': Entry.all_published.all()[:instance.count],
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(CMSLatestBlogEntriesPlugin)