from rest_framework import serializers
from .models import PasteBin
from user.models import User


class PasteSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source="user.email")
    class Meta:
        model=PasteBin
        fields = "__all__"
    


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = [

                "id","name","email"
            ]