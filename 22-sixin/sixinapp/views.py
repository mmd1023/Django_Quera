from .models import Musician, Album
from django.views.generic import ListView, DeleteView


class MusicianListView(ListView):
    model = Musician
    template_name = 'musician_list.html'
    paginate_by = 1
    queryset = Musician.objects.order_by('name')


class AlbumDetailView(DeleteView):
    model = Album
    template_name = 'album_detail.html'
    queryset = Album.objects.filter(num_stars__gte=3)
