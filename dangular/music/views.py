# from django.http import HttpResponse, Http404
from django.core.mail.backends import console

from .models import Albums, Song
# from django.template import loader
from django.shortcuts import render, get_object_or_404

# template loading using django loader
# def index(request):
#     all_albums = Albums.objects.all()
#     # html = ''
#     # for album in all_albums:
#     #     url = '/music/' + str(album.id) + '/'
#     #     html += '<a href="' + url + '">' + album.album_title+'</a><br>'
#     template = loader.get_template('music/index.html')
#     context = {
#         "all_albums": all_albums,
#     }
#     return HttpResponse(template.render(context, request))


# render template using django shortcuts
def index(request):
    all_albums = Albums.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)


# function with try catch to handle exception
# def album_detail(request, album_id):
#     try:
#         album = Albums.objects.get(id=album_id)
#     except Albums.DoesNotExist:
#         raise Http404("Album doesnt exists")
#     return render(request, 'music/detail.html', {'album': album})


def album_detail(request, album_id):
    album = get_object_or_404(Albums, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})


def favourite(request, album_id):
    album = get_object_or_404(Albums, pk=album_id)
    try:
        selected_songs = album.song_set.get(pk=request.POST['song'])
        print(selected_songs)
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': 'select a valid song'
        })
    else:
        # selected_songs.s
        selected_songs.is_favourite = True
        selected_songs.save
        return render(request, 'music/detail.html', {'album': album})


