from django.shortcuts import render
from mywatchlist.models import MyWatchlistItem

# Create your views here.

def show_mywatchlist(request):
    data_watchlist = mywatchlist.objects.all()
    context = {
    'list_movie': data_wathlist,
    'nama': 'Amanda',
    'Student ID': '2106637246',
}
    return render(request, "mywatchlist.html", context)