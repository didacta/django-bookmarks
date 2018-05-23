from django.shortcuts import render
from .models import Bookmark
# Create your views here.


def index(request):
    context = {
      'bookmark': Bookmark.objects.all(),
    }

    return render(request, 'bookmarks/index.html', context)
