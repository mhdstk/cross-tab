from django.contrib import admin
from django.urls import path
from web.views import *

urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
]
