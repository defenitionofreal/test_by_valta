from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """ User Serializer """

    class Meta:
        model = User
        fields = ('id', 'email')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("email", instance.email)
        instance.name = validated_data.get("first_name", instance.first_name)
        instance.name = validated_data.get("last_name", instance.last_name)
        instance.save()
        return instance

