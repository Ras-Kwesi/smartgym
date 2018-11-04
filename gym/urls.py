from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.user,name = 'user'),
    url(r'^trainer_login/$',views.trainer_login,name='trainer_login'),
    url(r'^client_login/$',views.client_login,name='client_login'),
    url(r'^manager_login/$',views.manager_login,name='manager_login'),
    url(r'^trainer_signup/$',views.trainer_signup,name='trainer_signup'),
    url(r'^client_signup/$',views.client_signup,name='client_signup'),
    url(r'^manager_signup/$',views.manager_signup,name='manager_signup'),
    url(r'^home/$',views.homepage,name = 'home'),

    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
