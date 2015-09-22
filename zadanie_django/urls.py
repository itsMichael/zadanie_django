from django.conf.urls import patterns, url
from users_base.views import AddUser, DeleteUser, UpdateUser


urlpatterns = patterns('',
        url(r'^/?$', 'users_base.views.home', name='home'),
        url(r'^add$', AddUser.as_view()),
        url(r'^remove/(?P<pk>[0-9]+)/$', DeleteUser.as_view()),
        url(r'^edit/(?P<pk>[0-9]+)/$', UpdateUser.as_view()),
        url(r'^generate$', 'users_base.views.generate_csv')
)
