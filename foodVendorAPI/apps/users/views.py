from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name', 'phone_number',
                  'password', 'is_customer', 'is_vendor')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        is_customer = validated_data.pop('is_customer')
        is_vendor = validated_data.pop('is_vendor')
        user = get_user_model().objects.create_user(**validated_data)
        user.is_customer = is_customer
        user.is_vendor = is_vendor
        user.save()
        return user


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
