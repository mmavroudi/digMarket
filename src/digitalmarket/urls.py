from django.conf.urls import include, url
from django.contrib import admin
from .views import home_view as home_view


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^$', home_view, name='home_view'),
    url(r'^create/$', 'products.views.create_view', name='create_view'),
    url(r'^detail/(?P<object_id>\d+)/edit/$', 'products.views.update_view', name='update_view'),
    url(r'^detail/(?P<object_id>\d+)/$', 'products.views.detail_view', name='detail_view'),
    url(r'^detail/(?P<slug>[\w-]+)/$', 'products.views.detail_slug_view', name='detail_slug_view'),
    url(r'^list/$', 'products.views.list_view', name='list_view'),
    url(r'^products/$', ProductListView.as_view(), name='product_list_view'),
    url(r'^products/add/$', ProductCreateView.as_view(), name='product_create_view'),
    url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail_view'),
    url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='product_detail_slug_view'),
    url(r'^products/(?P<pk>\d+)/edit/$', ProductUpdateView.as_view(), name='product_update_view'),
    url(r'^products/(?P<slug>[\w-]+)/edit/$', ProductUpdateView.as_view(), name='product_update_view'),
]
