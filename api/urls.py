from django.conf.urls import url
from api.views import UsersList 

urlpatterns = [
    url(r'^users/$', UsersList.as_view()),
]