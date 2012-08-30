from crud.views import UserListView, UserCreateView, UserUpdateView, \
    UserDeleteView
from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url (
         regex='^users/$',
         view=UserListView.as_view(),
         name='user_list'
         ),
    url (
         regex='^users/create/$',
         view=UserCreateView.as_view(),
         name='user_create',
         ),
    url (
         regex='^users/update/(?P<userId>\d+)/$',
         view=UserUpdateView.as_view(),
         name='user_update',
         ),
    url (
         regex='^users/delete/(?P<userId>\d+)/$',
         view=UserDeleteView.as_view(),
         name='user_delete',
         ),
)
