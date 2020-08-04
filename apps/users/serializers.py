from rest_framework import serializers
from .models import Users


class UsersSerializers(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    last_login = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = Users
        fields = "__all__"
