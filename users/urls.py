from django.urls import path, include,re_path
from django.urls import re_path as url

from . import views

from django.conf import settings
from django.conf.urls.static import static
from .views import *



app_name = 'users'

urlpatterns = [
   #path('signup/',views.signup,name="signup"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)