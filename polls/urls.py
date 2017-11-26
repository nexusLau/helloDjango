from django.conf.urls import url

from . import views
from . import search

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^hello$', views.hello, name='index'),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
]