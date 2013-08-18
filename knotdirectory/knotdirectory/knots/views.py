from django.views.generic import ListView, DetailView

from models import Knot


class KnotListView(ListView):
    model = Knot
    paginate_by = 40


class KnotDetailView(DetailView):
    model = Knot
