from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('', views.post_list),
    url(r'^api/post/$', views.post_list),
    url(r'^api/post/(?P<pk>[0-9]+)$', views.getPost),
]

