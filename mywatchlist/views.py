from django.shortcuts import render
from mywatchlist.models import MyWatchlistItem

from django.http import HttpResponse
from django.core import serializers


def show_mywatchlist(request):
    data = MyWatchlistItem.objects.all()
    context = {
    'list_movie': data,
    'nama': 'Amanda',
    'Student_ID': '2106637246',
}
    return render(request, "mywatchlist.html", context)

def Nampilin(request):
    data = MyWatchlistItem.objects.filter(watched_movie=True)
    context = {
    'list_movie': data,
    'nama': 'Amanda',
    'Student_ID': '2106637246',
}
    return render(request, "mywatchlist.html", context) 


def show_mywatchlist_xml(request):
    data = MyWatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_mywatchlist_json(request):
    data = MyWatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

