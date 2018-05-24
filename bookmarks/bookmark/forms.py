from django import forms 
from .models from Bookmark

class BookmarkForm(forms.ModelForm):

    class Meta:
      model = Bookmark
      fields =('url', 'name', 'notes')