from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from taggit.models import Tag
from braces.views import JSONResponseMixin

from models import Knot, CreatorProfile
from .forms import LinkFormset, KnotForm
from .inlineformsetsviews import InlineFormsetsCreateView
from .inlineformsetsviews import InlineFormsetsUpdateView


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


class CreateKnotView(InlineFormsetsCreateView):
    model = Knot
    form = KnotForm
    formsets = [LinkFormset, ]

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreateKnotView, self).dispatch(*args, **kwargs)


class UpdateKnotView(InlineFormsetsUpdateView):
    model = Knot
    form_class = KnotForm
    formsets = [LinkFormset, ]

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateKnotView, self).dispatch(*args, **kwargs)


class AutocompleteTagView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        q = self.request.GET.get('q', '')
        tags = Tag.objects.filter(name__istartswith=q)
        context = map(lambda x: {'id': x.name, 'text': x.name}, tags)
        return self.render_json_response(context)
