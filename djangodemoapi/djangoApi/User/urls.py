from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    url(r'^login/$',
        views.AuthenticateUser.as_view(),
        name='login'),

    url(r'^register/$',
        views.UserRegistrationAPIView.as_view(),
        name='register'),

    url(r'^password_reset/$', auth_views.PasswordResetView, name='password_reset'),

    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView, name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView, name='password_reset_confirm'),
    
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView, name='password_reset_complete'),

    url(r'^authenticate_email/$', views.AuthenticateEmail.as_view(), name="authenticate_email"),

    url(r'^bio/(?P<bio_id>\d+)/$', views.BioDetails.as_view(), name="bio"),
    
    url(r'^bio/$', views.BioDetails.as_view(), name="bio"),

    url(r'^privacy_setting/$', views.PrivacySetting.as_view(), name="privacy_setting"),

    url(r'^user_list/$', views.UserView.as_view(), name="privacy_setting"),

    # Api to get blocked and add blocked users with get and post method
    # url(r'^block_user/$', views.BlockUsers.as_view(), name="block_user"),
    # Api to delete blocked users
    # url(r'^remove_blocked_user/(?P<blockeduser_id>\d+)/$', views.BlockUsers.as_view(), name="remove_blocked_user"),

]