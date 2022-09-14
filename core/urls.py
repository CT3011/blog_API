from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls



urlpatterns = [
    # Oauth
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    # Project URLS
    path('admin/', admin.site.urls),
    path('', include('blog.urls'), name='blog'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Blog_API Applications
    path('api/', include('blog_api.urls'),name='blog_api'),
    # user Management
    path('api/user/', include('users.urls'), name='users'),
    
    # API scama and Documintations
    path('docs/', include_docs_urls(title='BlogAPI')),
    path('schema', get_schema_view(
        title='BlogAPI',
        description='API for the BlogAPI',
        version='1.0.0'
        
    ),name='openapi-schema'),

]
# image find settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
