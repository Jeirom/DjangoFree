from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, post_contacts    # path('', include('catalog.urls', namespace = app_name)),

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home),
    path('contacts/', post_contacts),
]
