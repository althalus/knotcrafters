from django.views.generic import ListView, DetailView

from models import Knot


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
