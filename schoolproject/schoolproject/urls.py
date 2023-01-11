from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include(('learning_materials.urls', 'learning_materials'), namespace='learning_materials')),
]
