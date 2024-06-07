from rest_framework import serializers
from django.contrib.auth.models import User

from referral_system.models import ReferralCode


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    referral_code = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'referral_code')

    def create(self, validated_data):
        referral_code = validated_data.pop('referral_code', None)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        if referral_code:
            try:
                referrer_code = ReferralCode.objects.get(code=referral_code, is_active=True)
                user.userprofile.referrer = referrer_code.user
                user.userprofile.save()
            except User.DoesNotExist:
                pass  # Handle the case where the referral code is invalid if necessary
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
