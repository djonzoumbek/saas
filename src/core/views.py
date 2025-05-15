from django.shortcuts import render
import pathlib
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).parent.resolve()

def home(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = qs.filter(path=request.path)
    my_title = "My Page"

    context = {
        "title": my_title,
        "visits_count": page_qs.count(),
        "percentage": (page_qs.count() * 100) / qs.count(),
        "total_visits": qs.count(),

    }

    PageVisit.objects.create(path=request.path)
    return render(request, "home.html", context)


def about(request, *args, **kwargs):
    my_title = "About Page"
    context = {
        "title": my_title,
    }
    return render(request, "about.html", context)