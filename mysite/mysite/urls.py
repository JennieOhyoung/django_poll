from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'mysite.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# )

# The url() function is passed four arguments, two required: regex and view, and two optional: kwargs, and name.

# urlpatterns = patterns('',
#     url(r'^polls/', include('polls.urls')),
#     url(r'^admin/', include(admin.site.urls)),
# )

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)