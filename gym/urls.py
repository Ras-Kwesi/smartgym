from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.index,name = 'landing'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^addgym/$', views.addgym, name='addgym'),
    url(r'^join/(\d+)$',views.join, name = 'join_gym'),
    url(r'^exitgym/(\d+)$', views.exitgym, name='exitgym'),
    url(r'^deletegym/(\d+)$',views.delgym, name = 'deletegym'),

    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
