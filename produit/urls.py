from rest_framework.routers import DefaultRouter
from .views import ProduitViewSet, CategorieViewSet

router = DefaultRouter()
router.register(r'categories', CategorieViewSet, basename='categorie')
router.register(r'', ProduitViewSet, basename='produit')

urlpatterns = router.urls
