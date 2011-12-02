from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('happy_blog.views',
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[\-\d\w]+)/$', EntryDetail.as_view(), name='happy_blog_entry_detail'),
)
