from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uitzendtender.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include('tender.api', namespace='api')),
    url(r'^tender/', include('tender.urls')),
    url(r'^inlener/', include('commissioner.urls')),
    url(r'^uitzendbureau/', include('agency.urls')),
    url(r'^bemiddelen/', include('tender.urls')),
)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
