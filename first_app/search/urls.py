from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SearchProductView.as_view(),name='query'),
    # url(r'products/(?P<slug>[\w-]+)/$', views.ProductDetailSlugView.as_view(),name='detail'),
]
