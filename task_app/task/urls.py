from django.conf.urls import url
from task import views
# from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^task/$', views.TaskList.as_view(), name='task'),
    url(r'^detail/<int:pk>/$', views.TaskDetail.as_view(), name='detail'),
    url(r'^create/$', views.TaskCreate.as_view(), name='create'),
]
