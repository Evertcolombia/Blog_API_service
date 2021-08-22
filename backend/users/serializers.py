from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class  UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "email", "password"]
        # extra_kwargs = {"password": {"write_only": True}}
        
    def create(self, validated_data):
        # name = validated_data["name"]
        email = validated_data["email"]
        password = validated_data["password"]
        user_obj = User.objects.create_user(email=email, password=password)
        user_obj.set_password(password)
        user_obj.save()
        return user_obj