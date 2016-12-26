from django.conf.urls.defaults import patterns, url
from simpletodo import views

urlpatterns = patterns(
    '',
    url('^$', views.index, name='todo_idx'),
    url('^new/$', views.new, name='todo_new'),
    url('^(?P<id>\d+)/edit/$', views.edit, name='todo_edit'),
    url('^(?P<id>\d+)/delete/$', views.delete, name='todo_delete'),
    url('^(?P<id>\d+)/finish/$', views.finish, name='todo_finish'),
)
