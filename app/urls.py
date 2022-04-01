from django.urls import path,include
from .views import *


urlpatterns = [
    path('',home,name="Home"),
    path('upload/',upload,name='upload'),
    path('register/',Signup,name="signup"),
    path('user/<str:name>',UsersPage,name="userPage"),
    path('Admin/',admin,name="Admin"),
    path('AdminReports/',AdminReports,name="AdminReport"),
    path('UserReports/<str:name>',UserReports,name="UserReport"),

]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)