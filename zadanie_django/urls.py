from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
        url(r'^/?$', 'users_base.views.home', name='home'),
        url(r'^add$', TemplateView.as_view(template_name="add.html")),
        url(r'^remove$', 'users_base.views.remove'),
        url(r'^edit$', 'users_base.views.edit', name='edit'),
        url(r'^generate$', 'users_base.views.generate_csv')
)
