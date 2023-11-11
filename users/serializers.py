from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "username",
            "password",
            "country_code",
            "contact_info",
            "document_type",
            "document_number",
            "role",
            "is_superuser",
            "reviews",
            "reservations"
        ]
        extra_kwargs = {"password": {"write_only": True}, "is_superuser": {"required": False, "default": False}, "reservations": {"required": False}}

    def create(self, validated_data):
        if validated_data["is_superuser"]:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance
