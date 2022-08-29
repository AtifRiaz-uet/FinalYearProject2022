# Import these methods
from urllib.request import urlopen

from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import redirect, render

from webapp.models import Image
import detect


def image_result(request):
    return render(request, 'result.html',)


def image_upload(request):
    context = dict()
    if request.method == 'POST':
        # username = request.POST["username"]
        image_path = request.POST["temp"]  # src is the name of input attribute in your html file, this src value is set in javascript code
        image = NamedTemporaryFile()
        image.write(urlopen(image_path).read())
        image.flush()
        image = File(image)
        name = str(image.name).split('\\')[-1]
        name = 'image.jpg'  # store image in jpeg format
        image.name = name
        if image is not None:
            obj = Image.objects.create(image=image)  # create a object of Image type defined in your model
            # obj.save()
            label_name = detect.main()
            # label_name = [("Board Marker","Brand: Dollar","Color: Black","Dimensions: 6' x 0.5'",)]
            # print(len(label_name))
            print(label_name)
            context["path"] = obj.image.url  #url to image stored in my server/local device
            url = obj.image.url
            if label_name == []:
                return render(request, 'nil.html', {"list": label_name, "image":url})
            else:
                if label_name.startswith("St"):
                    return render(request, 'pouch.html', {"list": label_name, "image":url})
                if label_name.startswith("Bla"):
                    return render(request, 'black_board.html', {"list": label_name, "image":url})
                if label_name.startswith("Re"):
                    return render(request, 'red_board.html', {"list": label_name, "image":url})
                if label_name.startswith("Blu"):
                    return render(request, 'blue_pointer.html', {"list": label_name, "image":url})
                if label_name.startswith("Do"):
                    return render(request, 'dol_pen.html', {"list": label_name, "image":url})
                if label_name.startswith("Or"):
                    return render(request, 'orange_high.html', {"list": label_name, "image":url})
                if label_name.startswith("Red_P"):
                    return render(request, 'red_point.html', {"list": label_name, "image":url})
                if label_name.startswith("Gum"):
                    return render(request, 'gum_stick.html', {"list": label_name, "image":url})
                if label_name.startswith("Ca"):
                    return render(request, 'cal.html', {"list": label_name, "image":url})
                if label_name.startswith("Gre"):
                    return render(request, 'green.html', {"list": label_name, "image":url})


            return render(request, 'red_board.html', {"list": label_name, "image":url})
        else :
            return redirect('/')
    return render(request, 'index.html', context=context)  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.