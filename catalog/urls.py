from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, post_contacts

app_name = CatalogConfig.name

urlpatterns = [
    # path('', include('catalog.urls', namespace = app_name)),
    path('home', home),
    path('contacts', post_contacts),
]
