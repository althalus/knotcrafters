from django.conf.urls import patterns, url

from .views import KnotListView, KnotDetailView

urlpatterns = patterns(
    '',
    url(r'^knots/', KnotListView.as_view()),
    url(r'^knot/(?P<pk>\d+)/', KnotDetailView.as_view()),

)
