from rest_framework.routers import DefaultRouter
from .views import CategoryView, NoutView



router = DefaultRouter()

router.register('categories', CategoryView, basename='categories')
router.register('car', NoutView, basename='nout')

urlpatterns = router.urls