from django.urls import path

from app.views import landingview
from .views import landingview, productlistview, supplierlistview, addsupplier, addproduct, \
    deleteproduct, confirmdeleteproduct, edit_product_post, edit_product_get

urlpatterns = [
    path('', landingview),

    # Products url´s
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
    

    # Supplier url´s
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
]
