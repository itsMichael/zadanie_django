from django.conf.urls import url
from users_base.views import AddUser, DeleteUser, UpdateUser, Home


urlpatterns = [
    url(r'^/?$', Home.as_view(), name='home'),
    url(r'^add$', AddUser.as_view(), name="add"),
    url(r'^remove/(?P<pk>[0-9]+)/$', DeleteUser.as_view(), name="remove"),
    url(r'^edit/(?P<pk>[0-9]+)/$', UpdateUser.as_view(), name="edit"),
    url(r'^generate$', 'users_base.views.generate_csv', name="generate"),
]
