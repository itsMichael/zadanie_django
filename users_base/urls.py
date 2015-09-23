from django.conf.urls import url
from users_base.views import UsersList 

urlpatterns = [
    url(r'^users/$', UsersList.as_view()),
]