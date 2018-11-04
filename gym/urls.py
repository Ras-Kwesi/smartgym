from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name='index'),
    # url('^$'),
    url('^chatroom/(\w+)$', views.chatroom, name='chatroom'),
    url('^post/(\w+)$', views.post, name='post'),
    url('^newchatroom/$', views.newchatroom, name='newchatroom'),
    url('^chatrooms/$', views.chatrooms, name='chatrooms'),
    url('^$',views.homepage,name = 'home'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
