from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from .views import home_view as home_view


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^$', home_view, name='home_view'),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


