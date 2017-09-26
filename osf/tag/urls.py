from django.conf.urls import  url, include
from views import *

urlpatterns = ( '',
    (r'^create/$', create_post),
    (r'^list/$', list_post ),
    (r'^edit/(?P<id>[^/]+)/$', edit_post),
    (r'^view/(?P<id>[^/]+)/$', view_post),
 )
