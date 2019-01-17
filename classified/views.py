from django.shortcuts import render
from django.views.generic import (
    DetailView,
    ListView,
)

from classified.models import (
    Classified,
    ViewCounter,
    NEW
)


class ClassifiedList(ListView):
    model = Classified
    paginate_by = 10


class ClassifiedDetail(DetailView):
    model = Classified

    def get_object(self):
        obj = super().get_object()
        ViewCounter.objects.create(classified=obj, state=NEW)
        return obj
