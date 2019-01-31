from django.urls import path

from .views import index   # TODO ask Dima about the way

urlpatterns = [
    path('index/', index),
]