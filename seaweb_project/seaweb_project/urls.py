from django.conf.urls import patterns, url, include
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import admin
admin.autodiscover()

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
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/home', login_required((TemplateView.as_view(template_name='registration/home.html'))),
                           name='accounts_home')
)
