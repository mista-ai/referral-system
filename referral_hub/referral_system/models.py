from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    referrer = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='referrals',
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username


class ReferralCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referral_codes')
    code = models.CharField(max_length=50, unique=True)
    expiration_date = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Automatically deactivate if the expiration date has passed
        if self.expiration_date < timezone.now():
            self.is_active = False

        # Deactivate other codes if this one is active
        if self.is_active:
            ReferralCode.objects.filter(user=self.user, is_active=True).update(is_active=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - {self.code}'
