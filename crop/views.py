from django.shortcuts import render, redirect

from .models import Photo
from .forms import PhotoForm
from PIL import Image

from django.core.files import File

def photo_list(request):
    photos = Photo.objects.all()
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.file_1 = form.cleaned_data.get("file")
            #photo_1 = data.file
            # print("x", photo)
            # print("y", data)
            # x = int(request.POST.get("x"))
            # y = int(request.POST.get("y"))
            # w = int(request.POST.get("width"))
            # h = int(request.POST.get("height"))
            # print(x, y, w, h)
            # y = data.y
            # w = data.width
            # h = data.height

            # image = Image.open(photo)
            # orginal = photo

            # cropped_image = image.crop((x, y, w + x, h + y))
            # resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
            #
            # data.file = resized_image(photo.path)
            # print('file',data.file)

            #data.file_1 = photo_1
            data.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'crop/photo_list.html', {'form': form, 'photos': photos})