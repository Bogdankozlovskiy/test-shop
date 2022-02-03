from django.urls import path
from product.views import RetrieveAPIItem, ListAPIItem


app_name = "Product"
urlpatterns = [
    path("items/", ListAPIItem.as_view(), name="list-item"),
    path("items/<int:pk>/", RetrieveAPIItem.as_view(), name="retrieve-item")
]
