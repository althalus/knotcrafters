from django.views.generic import ListView, DetailView

from models import Knot, CreatorProfile


class KnotListView(ListView):
    model = Knot
    paginate_by = 40

    def get_queryset(self):
        queryset = super(KnotListView, self).get_queryset()
        tag = self.kwargs.get('tag')
        if tag:
            queryset = queryset.filter(tags__name__in=[tag])
        return queryset


class KnotDetailView(DetailView):
    model = Knot


class CreatorListView(ListView):
    model = CreatorProfile
    paginate_by = 10

    def get_queryset(self):
        queryset = super(CreatorListView, self).get_queryset()
        queryset.prefetch_related('knot_set')
        return queryset


class CreatorDetailView(DetailView):
    model = CreatorProfile

    def get_queryset(self):
        queryset = super(CreatorDetailView, self).get_queryset()
        queryset.prefetch_related('knot_set')
        return queryset
