from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
        url(r'^', include('users_base.urls')),
        url(r'^api/', include('api.urls'))
)
