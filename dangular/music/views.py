from django.http import HttpResponse, Http404
from .models import Albums
# from django.template import loader
from django.shortcuts import render

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


def album_detail(request, album_id):
    try:
        album = Albums.objects.get(id= album_id)
    except Albums.DoesNotExist:
        raise Http404("Album doesnt exists")
    return render(request, 'music/detail.html', {'album': album})
