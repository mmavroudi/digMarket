from django.conf.urls import include, url
from django.contrib import admin
from .views import home_view as home_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^$', home_view, name='home_view'),
]
