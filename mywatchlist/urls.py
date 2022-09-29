from django.urls import path
from mywatchlist.views import show_mywatchlist

from mywatchlist.views import show_mywatchlist_xml

from mywatchlist.views import show_mywatchlist_json

from mywatchlist.views import Nampilin

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml'),
    path('json/', show_mywatchlist_json, name='show_mywatchlist_json'),
    path('udahditongton/', Nampilin, name='Nampilin')
]