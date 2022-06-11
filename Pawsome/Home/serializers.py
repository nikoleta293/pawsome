from rest_framework import serializers
from Users.models import Users

class VSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['password']