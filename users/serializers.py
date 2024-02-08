from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User, PurchaseHistory, Feedback

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["url", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user


class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = ['id', 'user', 'timestamp', 'total_amount']

class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'text']

