from django.conf.urls import url, include
from django.contrib import admin
from views import CreateBook, CreateAuthor, IndexShow, ShowBook, ShowAuthor, ChangeBook, ChangeAuthor
urlpatterns = [
    url(r'^create_book/$', CreateBook),
    url(r'^create_author/$', CreateAuthor),
    url(r'^index/$', IndexShow),
    url(r'^books/(\w+)/$', ShowBook),
    url(r'^authors/(\w+)/$', ShowAuthor),
    url(r'^books/change/(\w+)/$', ChangeBook),
    url(r'^authors/change/(\w+)/$', ChangeAuthor),
    url(r'^admin/', include(admin.site.urls)),
]
