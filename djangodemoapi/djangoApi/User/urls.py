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

    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),

    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    url(r'^authenticate_email/$', views.AuthenticateEmail.as_view(), name="authenticate_email"),

    url(r'^save_bio/$', views.BioDetails.as_view(), name="save_bio"),
    
    url(r'^edit_bio/<int:pk>$', views.UpdateDetails.as_view(), name="edit_bio")

]