from django.urls import path
from django.conf.urls import url
from .views import (HomeView, URLRedirectView)

app_name = "main"

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='homeview'),
    url(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='scode'),
 ]
