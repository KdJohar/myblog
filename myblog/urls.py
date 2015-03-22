from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blogs.views.index', name='home'),
    url(r'^blogs-category/$', 'blogs.views.category', name='category'),
    url(r'^blogs-category/(?P<slug>[\w-]+)/$', 'blogs.views.category_view', name='category_view'),
    url(r'^blog/(?P<slug>[\w-]+)/$', 'blogs.views.blog_view', name='blog_view'),
    #url(r'(?P<slug>[\w-]+)/^$', 'blogs.views.category_view', name='category'),
    # url(r'^blog/', include('blog.urls')),
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
