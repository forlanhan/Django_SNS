from django.conf.urls import  include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import settings

from filebrowser.sites import site

from views import *
urlpatterns = ['',
                          url(r'^admin/filebrowser/', include(site.urls)),
                          url( r'^grappelli/', include( 'grappelli.urls' ) ),  # grappelli URLS
                          url( r'^admin/', include( admin.site.urls ) ),
                          url( r'^accounts/', include('userena.urls'),),
                          url( r'^account/',include('accounts.urls')),


                        url( r'^$', showHomePage),
                        url( r'^explore/$', explore),
                        url( r'^welcome/$', welcome),
                        url( r'^followers$', get_followers),
                        url( r'^followings$',get_followings),
                        url( r'^user/(?P<id>[^/]+)$',user_index),

    # Examples:
    # url(r'^$', 'depot.views.home', name='home'),
    # url(r'^depot/', include('depot.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

 ]



urlpatterns += ('',url(r'^post/', include('post.urls')),)
urlpatterns += ('',url(r'^spost/', include('spost.urls')),)
urlpatterns += ('',url(r'^album/', include('album.urls')),)
urlpatterns += ('',url(r'^comment/', include('comment.urls')),)
urlpatterns += ('',url(r'^tag/', include('tag.urls')),)
urlpatterns += ('',url(r'^notifications/', include('notification.urls')),)
urlpatterns += ('',url(r'^like/', include('like.urls')),)
urlpatterns += ('',url( r'^follow/', include('follow.urls'),),)
urlpatterns += ('',url(r'^api/', include('restapi.urls')),)
#urlpatterns += patterns('',url(r'^user/', include('accounts.urls')),)

urlpatterns += staticfiles_urlpatterns()


# if settings.DEBUG:
#     urlpatterns += patterns( '', url( r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT } ),
#     url( r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT} ), )


urlpatterns += [ url( r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT } ),
url( r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT} ), ]
    
