from django.conf.urls import patterns, include, url
from django.contrib import admin
from commissioner import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uitzendtender.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
  

)

