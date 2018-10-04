from django  import forms

from .models import Photos

class PhotoUploadform(forms.ModelForm):
  class Meta:
    model = Photos
    fields = (
      'title',
      'ImagePhoto',
      "Description"
    )

