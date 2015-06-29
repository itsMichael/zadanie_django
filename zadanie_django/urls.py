from django.conf.urls import patterns, url

urlpatterns = patterns('',
        url(r'^/?$', 'users_base.views.home'),
        url(r'^add$', 'users_base.views.add'),
)
