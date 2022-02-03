from rest_framework.generics import CreateAPIView

from root.serializers import CreateUserSerializer
from product.models import Bucket


class Register(CreateAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user_id = response.data['id']
        bucket = Bucket.objects.get(owner_id=user_id)
        response.set_cookie("bucket", bucket.id)
        return response

