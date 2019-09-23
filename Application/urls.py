from django.urls import path
from Application.views import index, product_view, size_view
urlpatterns = [
    path('size/<str:category_slug>/', size_view, name='size_detail'),
    path('product/<str:product_slug>/', product_view, name='product_detail'),
    # path(r'^product/(?P<product_slug>[-\w]+)/$', product_view, name='product_detail'),
    # path(r'^size/(?P<size_slug>[-\w]+)/$', size_view, name='size_detail'),
    # path('^size/(?P<size_slug>[-\w]+)/$',size_view,name='size_detail'),
    # path('^product/(?P<product_slug>[-\w]+)/$',product_view,name='product_detail'),
    path('', index, name='index'),

]
