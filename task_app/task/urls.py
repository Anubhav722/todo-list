from django.conf.urls import url
from task import views
# from django.contrib.auth import views as auth_views

# app_name = 'task'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^task/$', views.TaskList.as_view(), name='task'),
    url(r'^detail/(?P<pk>\d+)/$', views.TaskDetail.as_view(), name='detail'),
    url(r'^create/$', views.TaskCreate.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.TaskUpdate.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.TaskDelete.as_view(), name='delete'),
    url(r'users/$', views.UserList.as_view(), name='users')
]
