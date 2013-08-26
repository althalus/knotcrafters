from django.conf.urls import patterns, url

from .views import KnotListView, KnotDetailView, CreatorListView, CreatorDetailView, CreateKnotView, UpdateKnotView

urlpatterns = patterns(
    '',
    url(r'^knots/$', KnotListView.as_view(), name="knots.list"),
    url(r'^knots/(?P<tag>.+)/', KnotListView.as_view(), name="knots.list_by_tag"),
    url(r'^knot/(?P<pk>\d+)/', KnotDetailView.as_view(), name="knots.detail"),
    url(r'^creators/', CreatorListView.as_view(), name="creators.list"),
    url(r'^creator/(?P<pk>\d+)/', CreatorDetailView.as_view(), name="creators.detail"),
    url(r'add/', CreateKnotView.as_view(), name='knots.create'),
    url(r'update/(?P<pk>\d+)/', UpdateKnotView.as_view(), name='knots.update')

)
