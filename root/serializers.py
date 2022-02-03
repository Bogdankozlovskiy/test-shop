from rest_framework.serializers import Serializer, CharField, EmailField, ValidationError, IntegerField
from django.contrib.auth import get_user_model
from product.models import Bucket

User = get_user_model()


class CreateUserSerializer(Serializer):
    username = CharField(required=True)
    first_name = CharField(required=False, default="")
    last_name = CharField(required=False, default="")
    email = EmailField(required=True)
    phone = CharField(required=False)

    password_1 = CharField(required=True, write_only=True)
    password_2 = CharField(required=True, write_only=True)

    id = IntegerField(read_only=True)

    def validate(self, attrs):
        if attrs['password_1'] != attrs['password_2']:
            raise ValidationError(detail="password must be equals")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone=validated_data.get('phone'),
            password=validated_data['password_1']
        )
        Bucket.objects.create(owner=user)
        return user
