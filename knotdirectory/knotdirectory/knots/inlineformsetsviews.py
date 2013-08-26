from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView


class FormsetsMixin(object):
    formsets = []

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formsets = self.get_formsets()

        context_data = self.get_context_data(form=form, formsets=formsets)
        return self.render_to_response(context_data)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formsets = self.get_formsets(request.POST)
        if form.is_valid() and all([x.is_valid() for x in formsets]):
            return self.form_valid(form, formsets)
        else:
            if not form.is_valid(): print "The base form is wrong"
            for forma in formsets:
                if not forma.is_valid():
                    print "Formset problem"
                    for formb in forma.forms:
                        print formb.errors
            return self.form_invalid(form, formsets)

    def form_valid(self, form, formsets):
        self.object = form.save()
        for formset in formsets:
            formset.instance = self.object
            formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formsets):
        contextdata = self.get_context_data(form=form, formsets=formsets)
        return self.render_to_response(contextdata)

    def get_formsets(self, post=None):
        return [x(post, instance=self.object) for x in self.formsets]


class InlineFormsetsCreateView(FormsetsMixin, CreateView):
    def get(self, request, *args, **kwargs):
        self.object = None
        return super(InlineFormsetsCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        return super(InlineFormsetsCreateView, self).post(request, *args, **kwargs)



class InlineFormsetsUpdateView(FormsetsMixin, UpdateView):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(InlineFormsetsUpdateView, self).get(request, *args, **kwargs)
