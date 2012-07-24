from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^resources/$', 'fakeapi.api.views.add_instance'),  # post
    url(r'^resources/(?P<name>[\w-]+)/$', 'fakeapi.api.views.bind_or_remove_instance'),  # post and delete
    url(r'^resources/(?P<name>[\w-]+)/host/(?P<host>[\w.]+)/$', 'fakeapi.api.views.unbind'),  # delete
)
