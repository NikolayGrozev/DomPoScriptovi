from django.shortcuts import render, HttpResponse
from .models import Count


def count(request):
    count = Count.objects.first()
    return render(request, "count.html", {"count": count} )