from django.conf.urls import  url, include
from views import *

urlpatterns = [

    (r'do$', dolike),
    (r'undo$', undolike),
 ]
