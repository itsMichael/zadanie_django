from django.conf.urls import patterns, url

urlpatterns = patterns('',
        url(r'^/?$', 'users_base.views.home'),
        url(r'^add$', 'users_base.views.add'),
        url(r'^remove$', 'users_base.views.remove'),
        url(r'^edit$', 'users_base.views.edit'),
)
