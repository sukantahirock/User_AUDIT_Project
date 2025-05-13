from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import CustomUser, UserProfile, AuditLog

@receiver(post_save, sender=CustomUser)
def handle_user_create(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        send_mail(
            'Welcome!',
            f'Hi {instance.username}, welcome to the site!',
            'admin@example.com',
            [instance.email],
            fail_silently=True
        )
        AuditLog.objects.create(user=instance, action='create', model_name='CustomUser', object_id=instance.id)
    else:
        AuditLog.objects.create(user=instance, action='update', model_name='CustomUser', object_id=instance.id)

@receiver(post_delete, sender=CustomUser)
def handle_user_delete(sender, instance, **kwargs):
    AuditLog.objects.create(user=None, action='delete', model_name='CustomUser', object_id=instance.id)
