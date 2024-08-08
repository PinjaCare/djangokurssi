from django.urls import path

from app.views import landingview
from .views import landingview, productlistview, supplierlistview, addsupplier, addproduct, \
    deleteproduct, confirmdeleteproduct

urlpatterns = [
    path('', landingview),

    # Products url´s
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    

    # Supplier url´s
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
]
