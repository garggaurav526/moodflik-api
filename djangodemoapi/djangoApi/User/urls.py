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

    url(r'^password_reset/$', views.PasswordResetReq.as_view(), name="password_reset"),
    url(r'^otp_validate/$', views.ValidateOTP.as_view(), name="otp_validate"),
    url(r'^reset_pass/$', views.ResetPassword.as_view(), name="reset_pass"),

    url(r'^authenticate_email/$', views.AuthenticateEmail.as_view(), name="authenticate_email"),
    
    url(r'^bio/$', views.BioDetails.as_view(), name="bio"),

    url(r'^privacy_setting/$', views.PrivacySetting.as_view(), name="privacy_setting"),
    
    url(r'^bio_setting/$', views.BioSetting.as_view(), name="bio_setting"),
    
    url(r'^show_figures/$', views.ShowingFiguresSettings.as_view(), name="show_figures"),

    url(r'^user_details/(?P<user_id>\d+)/$', views.UserView.as_view(), name="privacy_setting"),

    # Api to get blocked and add blocked users with get and post method
    url(r'^block_user/$', views.BlockUsers.as_view(), name="block_user"),
    # Api to delete blocked users
    url(r'^remove_blocked_user/(?P<blockeduser_id>\d+)/$', views.BlockUsers.as_view(), name="remove_blocked_user"),

    url(r'^contact_us/$', views.ContactAPIView.as_view(), name='contact_us'),

]