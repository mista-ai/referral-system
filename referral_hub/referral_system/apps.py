from django.apps import AppConfig


class ReferralSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'referral_system'

    def ready(self):
        import referral_system.signals
