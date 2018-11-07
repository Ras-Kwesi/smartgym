from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name='landing'),
    # url('^$'),
    url('^chatroom/(\w+)$', views.chatroom, name='chatroom'),
    url('^post/(\w+)$', views.post, name='post'),
    url('^newchatroom/$', views.newchatroom, name='newchatroom'),
    url('^chatrooms/$', views.chatrooms, name='chatrooms'),
    url(r'^trainer_login/$',views.trainer_login,name='trainer_login'),
    url(r'^client_login/$',views.client_login,name='client_login'),
    url(r'^manager_login/$',views.manager_login,name='manager_login'),
    url(r'^trainer_signup/$',views.trainer_signup,name='trainer_signup'),
    url(r'^client_signup/$',views.client_signup,name='client_signup'),
    url(r'^manager_signup/$',views.manager_signup,name='manager_signup'),
    url(r'^home/$',views.homepage,name = 'home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^addgym/$', views.addgym, name='addgym'),
    url('^joinchat/(\d+)', views.joinchat, name='joinchat'),
    url('^exitchat/(\d+)', views.exitchatroom, name='exitchat'),
    url('profile/$', views.profile, name='profile'),

    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
