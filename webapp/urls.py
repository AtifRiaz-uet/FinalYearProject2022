from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from webapp import views

urlpatterns = [
    path('', views.image_upload, name='image_upload'),
    path('result', views.image_result, name='image_result'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)