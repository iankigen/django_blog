from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'full_name', 'email',
            'date_joined', 'last_login'
        )

        extra_kwargs = {
            'date_joined': {'read_only': True},
            'last_login': {'read_only': True},
        }

    def get_full_name(self, obj):
        return "{} {}".format(
            obj.first_name,
            obj.last_name
        )
