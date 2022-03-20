
from django.urls import path

from . import views
from . import apis


urlpatterns = [
    # views
    path('index', views.index, name='index'),
    # apis
    path('post', apis.post_api, name='post'),
]