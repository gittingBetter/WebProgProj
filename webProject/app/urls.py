from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^login/$', views.login_user, name = 'login'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^logout/$', views.logout_user, name = 'logout'),
    url(r'^profile/(?P<uname>[\w|\W.-]+)/$', views.user_details, name = 'profile'),
    url(r'^del_user/(?P<uname>[\w|\W.-]+)/$', views.remove_user, name='removeUser'),

    #url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name = 'logout'),
]
