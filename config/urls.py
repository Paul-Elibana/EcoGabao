from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/comptes/', include('comptes.urls')),
    path('api/blog/', include('blog.urls')),
    path('api/produits/', include('produit.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
