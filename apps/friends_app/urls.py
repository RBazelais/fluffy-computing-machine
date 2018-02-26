from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.friends),
    url(r'^add/(?P<id>\d+)$', views.add_friend),
    url(r'^remove/(?P<id>\d+)$', views.remove_friend),
    url(r'^user/(?P<id>\d+)$', views.profile)
]