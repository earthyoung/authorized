from rest_framework import serializers

from authorized.account.models import Authority, Ownership, Record, User, House


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
    user = serializers.IntegerField()
    house = serializers.IntegerField()

    class Meta:
        model = Ownership
        fields = "__all__"


class AuthoritySerializer(serializers.ModelSerializer):
    user = serializers.IntegerField()
    house = serializers.IntegerField()

    class Meta:
        model = Authority
        fields = "__all__"


class RecordSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField()
    house = serializers.IntegerField()

    class Meta:
        model = Record
        fields = "__all__"
