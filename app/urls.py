from django.urls import path,include
from .views import *


urlpatterns = [
    path('',person_image_view),
    path('success', success, name = 'success'),
    path('markAtt/',MarkAttendance),
    path('present/<str:name>/',present),
    path('capturePhoto/',CapturePhoto)
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

