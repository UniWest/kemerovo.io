
from django.contrib import admin
from django.urls import path
from myservice import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
]
