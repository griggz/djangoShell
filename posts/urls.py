from django.urls import path, re_path, include
from . import views

app_name = 'posts'

urlpatterns = [
    re_path(r'^$', views.posts_list, name='list'),
    re_path(r'^create/$', views.posts_create, name='create'),
    re_path(r'^detail/(?P<slug>[\w-]+)/$', views.posts_detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', views.posts_update, name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', views.posts_delete, name='delete'),
]
