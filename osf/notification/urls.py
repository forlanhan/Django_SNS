from django.conf.urls import  url, include
from views import *

urlpatterns = [

    (r'comment/$', comment),
    (r'follow/$', follow),
    (r'like/$', like),
    (r'system/$', system),

]
