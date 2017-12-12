from photo.models import Album, Photo
from django.forms.models import inlineformset_factory

PhotoInlineFormSet = inlineformset_factory(Album, Photo,
    fields = ['image','image', 'title', 'description'],
    extra = 2)
