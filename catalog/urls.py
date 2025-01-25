from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, post_contacts, product_info, product_index

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home),
    path('contacts/', post_contacts),
    path('product_info/', product_index),
]
