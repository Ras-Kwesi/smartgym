from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^(\d+)$',views.index,name='landing'),
    # url('^$'),
    url('^chatroom/(\d+)$', views.chatroom, name='chatroom'),
    url('^chatroom/(\d+)$', views.chat, name='chats'),
    url(r'^join_chatroom/(\d+)$',views.join_chatroom, name = 'joinchatroom'),
    url('^post/(\d+)$', views.post, name='post'),
    url('^newchatroom/$', views.newchatroom, name='newchatroom'),
    url('^chatrooms/$', views.chatrooms, name='chatrooms'),
    url(r'^join/(\d+)$',views.join, name = 'join'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^addgym/$', views.addgym, name='addgym'),
    url('^joinchat/(\d+)', views.joinchat, name='joinchat'),
    url('^exitchat/(\d+)', views.exitchatroom, name='exitchat'),
    url('profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^user/(\d+)$', views.myprofile, name='profile'),
    url('^viewgyms/$', views.view_gyms, name='viewgyms'),

    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
