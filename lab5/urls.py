from django.conf.urls import patterns, include, url
from blog.views import test_home
from blog.views import test_help
from blog.views import test_about

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^home/$', test_home),
    url(r'^help/$', test_help),
    url(r'^about/$', test_about),
    # Examples:
    # url(r'^$', 'lab5.views.home', name='home'),
    # url(r'^lab5/', include('lab5.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


    