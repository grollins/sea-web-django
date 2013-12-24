from django.conf.urls import patterns, url, include
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib import admin
admin.autodiscover()

from registration.backends.default.views import ActivationView
from registration.backends.default.views import RegistrationView

from rest_framework.routers import DefaultRouter
from jobs.views import JobViewSet, UserViewSet, ResultViewSet


router = DefaultRouter()
router.register(r'jobs', JobViewSet, base_name='job')
router.register(r'results', ResultViewSet)
router.register(r'users', UserViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns += patterns('',
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token')
)

urlpatterns += patterns('backend.views',
                       url(r'^admin/', include(admin.site.urls))
)

urlpatterns += patterns('',
    url(r'^accounts/login/$', auth_views.login,
        {'template_name': 'registration/login.html'},
        name='auth_login'),
    url(r'^accounts/logout/$', auth_views.logout,
        {'template_name': 'registration/home.html'},
        name='auth_logout'),
    url(r'^accounts/password/change/$', auth_views.password_change,
        name='password_change'),
    url(r'^accounts/password/change/done/$', auth_views.password_change_done,
        name='password_change_done'),
    url(r'^accounts/password/reset/$', auth_views.password_reset,
        name='password_reset'),
    url(r'^accounts/password/reset/done/$', auth_views.password_reset_done,
        name='password_reset_done'),
    url(r'^accounts/password/reset/complete/$', auth_views.password_reset_complete,
        name='password_reset_complete'),
    url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^accounts/home/$',
        TemplateView.as_view(template_name='registration/home.html'),
        name='accounts_home'),
    url(r'^accounts/activate/complete/$',
        TemplateView.as_view(template_name='registration/activation_complete.html'),
        name='registration_activation_complete'),
        # Activation keys get matched by \w+ instead of the more specific [a-fA-F0-9]{40} because a bad activation key should still get to the view; that way it can return a sensible "invalid key" message instead of a confusing 404.
    url(r'^accounts/activate/(?P<activation_key>\w+)/$', ActivationView.as_view(),
        name='registration_activate'),
    url(r'^accounts/register/$', RegistrationView.as_view(),
        name='registration_register'),
    url(r'^accounts/register/complete/$',
        TemplateView.as_view(template_name='registration/registration_complete.html'),
        name='registration_complete'),
    url(r'^accounts/register/closed/$',
        TemplateView.as_view(template_name='registration/registration_closed.html'),
        name='registration_disallowed'),
)

