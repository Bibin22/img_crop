from PIL import Image
from django import forms
from django.core.files import File
from .models import Photo

class PhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())
    file_1 = forms.ImageField(widget=forms.HiddenInput(), required=False)


    class Meta:
        model = Photo
        fields = ('file', 'x', 'y', 'width', 'height',)

    def save(self, commit):
        photo = super(PhotoForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.file)

        cropped_image = image.crop((x, y, w + x, h + y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)

        resized_image.save(photo.file.path)
        return photo


