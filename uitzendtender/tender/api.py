from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from agency import views as agency_views
from commissioner import views as commissioner_views
import views as tender_views


user_list = commissioner_views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = commissioner_views.UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = patterns('',
    url(r'^inlener/detail/(?P<pk>[0-9]+)/$', commissioner_views.CompanyDetailApi.as_view(),
        name='commissioner_detail_view'),
    url(r'^inlener/contact/(?P<pk>[0-9]+)/$', commissioner_views.ContactDetailApi.as_view(),
        name='commissioner_contact_view'),
    url(r'^inlener/gebruikers/$', user_list, name='commissioner_users_overview'),
    url(r'^inlener/gebruiker/(?P<pk>[0-9]+)/$', user_detail,
        name='commissioner_user_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)

