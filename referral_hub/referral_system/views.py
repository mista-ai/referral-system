from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.utils import timezone
from .models import ReferralCode
from .serializers import ReferralCodeSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReferralCodeCreateView(generics.CreateAPIView):
    queryset = ReferralCode.objects.all()
    serializer_class = ReferralCodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ReferralCodeDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        try:
            referral_code = ReferralCode.objects.get(user=user, is_active=True)
            referral_code.delete()
            return Response(status=204)
        except ReferralCode.DoesNotExist:
            return Response(status=404)


class ReferralCodeActivateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        code_id = kwargs.get('pk')
        try:
            referral_code = ReferralCode.objects.get(id=code_id, user=user)
            # Deactivate other codes
            ReferralCode.objects.filter(user=user, is_active=True).update(is_active=False)
            # Activate the selected code
            referral_code.is_active = True
            if referral_code.expiration_date < timezone.now():
                return Response({'detail': 'Referral code has expired.'}, status=status.HTTP_400_BAD_REQUEST)
            referral_code.save()
            return Response({'detail': 'Referral code activated successfully.'}, status=status.HTTP_200_OK)
        except ReferralCode.DoesNotExist:
            return Response({'detail': 'Referral code not found.'}, status=status.HTTP_404_NOT_FOUND)


class ReferralCodeListView(generics.ListAPIView):
    serializer_class = ReferralCodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ReferralCode.objects.filter(user=self.request.user)
