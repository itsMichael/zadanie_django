from django.conf.urls import patterns, url, include
from users_base.views import AddUser, DeleteUser, UpdateUser, Home


urlpatterns = patterns('',
        url(r'^/?$', Home.as_view(), name='home'),
        url(r'^add$', AddUser.as_view()),
        url(r'^remove/(?P<pk>[0-9]+)/$', DeleteUser.as_view()),
        url(r'^edit/(?P<pk>[0-9]+)/$', UpdateUser.as_view()),
        url(r'^generate$', 'users_base.views.generate_csv'),
        url(r'^api-auth/', include('users_base.urls'))
)
