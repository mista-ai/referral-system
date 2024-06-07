from rest_framework import serializers
from django.contrib.auth.models import User

from referral_system.models import ReferralCode


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class ReferralCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralCode
        fields = ['id', 'code', 'expiration_date', 'is_active']
        read_only_fields = ['id']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        referral_code = ReferralCode.objects.create(**validated_data)
        return referral_code
