from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, post_contacts, product_info, product_index, product_action

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home),
    path('contacts/', post_contacts),
    path('product_info/', product_index),
    path('product_action/',product_action),
]
