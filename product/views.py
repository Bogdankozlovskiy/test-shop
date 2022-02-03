from product.serializers import ListItemSerializer, RetrieveItemSerializer
from product.models import Item

from rest_framework.generics import RetrieveAPIView, ListAPIView


class ListAPIItem(ListAPIView):
    serializer_class = ListItemSerializer
    queryset = Item.objects.all()


class RetrieveAPIItem(RetrieveAPIView):
    serializer_class = RetrieveItemSerializer
    queryset = Item.objects.all()
