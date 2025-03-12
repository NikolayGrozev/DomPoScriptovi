from django.shortcuts import render, HttpResponse
from .models import Count


def count(request):
    count = Count.objects.first()
    count.ammount += 1
    count.save()
    return render(request, "count.html", {"count": count} )