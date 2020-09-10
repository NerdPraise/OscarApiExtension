from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from oscarapi.serializers.login import field_length, UserSerializer


User = get_user_model()


class UserViewSerializer(UserSerializer):
    """
    An extension of oscarapi serializer
    """
    first_name = serializers.CharField(
        max_length=field_length("first_name"), required=True)
    last_name = serializers.CharField(
        max_length=field_length("last_name"), required=True)
    username = serializers.CharField(
        max_length=field_length("username"), required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = UserSerializer.Meta.fields + (
            "first_name", "last_name", "username", "email", "password")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            "first_name", instance.first_name)
        instance.last_name = validated_data.get(
            "last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        if validated_data["password"]:
            instance.password = make_password(validated_data.get("password"))
        instance.save()
        return instance
