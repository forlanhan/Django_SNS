from django.conf.urls import  url, include
from views import *

urlpatterns = [
    (r'^setting/info$', settingInfoPage),
     (r'^setting/avatar$', settingAvatar),
     (r'^setting/security$', settingSecurity),
    (r'^setting/changepw', resetpwdPage),
    (r'^setting/changeavatar', changeavatar),
 ]
