from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path 
from django.urls import re_path
from django.views.static import serve

# from django.conf import settings
# from django.urls import re_path
# from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("ecommerce.apps.catalogue.urls", namespace="catalogue")),
    path("checkout/", include("ecommerce.apps.checkout.urls", namespace="checkout")),
    path("basket/", include("ecommerce.apps.basket.urls", namespace="basket")),
    path("account/", include("ecommerce.apps.account.urls", namespace="account")),
    path("orders/", include("ecommerce.apps.orders.urls", namespace="orders")),
]


# ... the rest of your URLconf goes here ...

# if settings.DEBUG:
#     urlpatterns += [
#          re_path(r'^media/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#     ]
   
   # Added Following Two Lines Of Code
# if settings.DEBUG:
#        url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
#        url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
