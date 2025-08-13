from rest_framework.routers import DefaultRouter

from apps.dds import views

app_name = "dds"
urlpatterns = []

router = DefaultRouter()
router.register("transaction", views.Transaction, basename="transaction")
router.register("category", views.Category, basename="category")
router.register("subcategory", views.Subcategory, basename="subcategory")
router.register("type", views.Type, basename="type")

urlpatterns += router.urls
