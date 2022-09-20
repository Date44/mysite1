from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", index),
    path("index", index),
    path("create", create),
    re_path(r"^details/(?P<post_id>[0-9]+)$", details),
]
