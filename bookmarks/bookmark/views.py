from django.shortcuts import render
from .models import Bookmark, PersonalBookmark
from .forms import BookmarkForm
# Create your views here.


def index(request):
    if request.method == 'POST':
      form = BookmarkForm(request.POST)
      if form.is_valid():
          form.save()
      else:
          pass

    context = {}

    pbid = PersonalBookmark.objects.values_list('id')

    context['bookmarks'] = Bookmark.objects.exclude(id_in=pbid) 

    if request.user.is_anonymous:
       context['personal_bookmarks'] = PersonalBookmark.objects.none()
    else:
       context['personal_bookmarks'] = PersonalBookmark.objects.filter(user=request.user)

    context['form'] = BookmarkForm
    return render(request, 'bookmarks/index.html', context)
