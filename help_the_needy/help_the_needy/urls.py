from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'help_the_needy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^map', 'help_the_needy.views.map'),
	url(r'^map2', 'help_the_needy.views.map2'),
    url(r'^admin/', include(admin.site.urls)),
)
