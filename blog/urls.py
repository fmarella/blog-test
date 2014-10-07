
from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.PostListView.as_view(), name='post-list'),
    url(r'^new$', views.PostCreateView.as_view(), name='post-new'),
    url(r'^(?P<pk>[-_\w]+)/$', views.PostDetailView.as_view(), name='post-detail'),
    url(r'^(?P<pk>[-_\w]+)/update/$', views.PostUpdateView.as_view(), name='post-update'),
)
