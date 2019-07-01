from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^accounts/profile/$', views.profile, name = 'profile'),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'^project/',views.project, name = 'project'),
    url(r'^search/',views.search, name='search'),
    url(r'^new_project/',views.new_project, name='new_project'),
    # url(r'^review/$',views.new_review, name='review'),
]     

if settings.DEBUG:
   urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
