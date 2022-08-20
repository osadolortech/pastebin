from rest_framework import serializers
from .models import PasteBin
from user.models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction


class PasteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.email")
    class Meta:
        model=PasteBin
        fields = "__all__"
    


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = [

                "id","name","email"
            ]
        read_only_fields = ('id','email')

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=120)

    @transaction.atomic
    def save(self, request):
        user= super().save(request)
        user.name=self.data.get('name')
        user.save()
        return user