from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'products/$', views.ProductListView.as_view(),name='list'),
    url(r'products/(?P<slug>[\w-]+)/$', views.ProductDetailSlugView.as_view(),name='detail'),
]
