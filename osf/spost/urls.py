from django.conf.urls import url, include
from views import *

urlpatterns = [
    (r'^create$', create_spost),
    (r'^list/$', list_spost ),
    (r'^edit/(?P<id>[^/]+)/$', edit_spost),
    (r'^view/(?P<id>[^/]+)/$', view_spost),
 ]
