from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^$', 'blog.views.profile', name='profile'),
    # url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
    url(r'^profile/(?P<user>.+)/$', 'blog.views.profile', name='Profile'),
    url(r'^login/$', 'blog.views.user_login', name='login'),
    url(r'^logout/$', 'blog.views.user_logout', name='logout'),
    url(r'^register/$', 'blog.views.register', name='register'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
