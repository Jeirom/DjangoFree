
from django.urls import path, include
from catalog.apps import CatalogConfig
from SkyBlog.views import SkyBlogListView, SkyBlogCreateView, SkyBlogUpdateView, SkyBlogDetailVIew, SkyBlogDeleteView

app_name = 'SkyBlog'

urlpatterns = [
    path('myblog/', SkyBlogListView.as_view(), name='myblog_list'),
    path('myblog/<int:pk>/', SkyBlogDetailVIew.as_view(), name='myblog_detail'),
    path('myblog/new/', SkyBlogCreateView.as_view(), name='myblog_create'),
    path('myblog/<int:pk>/edit/', SkyBlogUpdateView.as_view(), name='myblog_edit'),
    path('myblog/<int:pk>/delete/', SkyBlogDeleteView.as_view(), name='myblog_delete'),
]
