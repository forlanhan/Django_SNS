from django.conf.urls import url, include
from views import *

urlpatterns = [
    (r'^(?P<id>[^/]+)$', dofollow),
    (r'^undo/(?P<id>[^/]+)$', undofollow),
 ]
