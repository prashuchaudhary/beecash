from rest_framework import routers
from ledger.views.transaction_view import TransactionViewSet

router = routers.DefaultRouter()
router.register("transaction", TransactionViewSet, basename="transaction-view")

urlpatterns = router.urls
