from django.urls import path
from referral_system import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('referral/create/', views.ReferralCodeCreateView.as_view(), name='referral_create'),
    path('referral/delete/', views.ReferralCodeDeleteView.as_view(), name='referral_delete'),
    path('referral/activate/<int:pk>/', views.ReferralCodeActivateView.as_view(), name='referral_activate'),
    path('referral/list/', views.ReferralCodeListView.as_view(), name='referral_list'),
]
