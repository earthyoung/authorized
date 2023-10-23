from rest_framework import serializers

from account.models import *


class UserSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = User
        fields = "__all__"


class HouseSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = House
        fields = "__all__"


class OwnershipSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    house = HouseSerializer()

    class Meta:
        model = Ownership
        fields = ["id", "user", "house", "created_at"]


class AuthoritySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    house = HouseSerializer()

    class Meta:
        model = Authority
        fields = ["id", "user", "house", "allowed_at", "disabled_at", "created_at"]


class RecordSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    house = HouseSerializer()

    class Meta:
        model = Record
        fields = ["id", "user", "house", "created_at"]


class OwnershipRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    house = HouseSerializer()

    class Meta:
        model = OwnershipRequest
        fields = ["id", "user", "house", "created_at"]


class AuthorityRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    house = HouseSerializer()

    class Meta:
        model = AuthorityRequest
        fields = ["id", "user", "house", "created_at"]

