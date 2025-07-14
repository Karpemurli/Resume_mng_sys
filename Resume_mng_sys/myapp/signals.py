import random
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser

def generate_otp():
    return str(random.randint(100000, 999999))

@receiver(pre_save, sender=CustomUser)
def handle_user_update(sender, instance, **kwargs):
    if not instance.pk:
        return  # New user, not an update

    try:
        old_user = CustomUser.objects.get(pk=instance.pk)
    except CustomUser.DoesNotExist:
        return

    changes = []

    # Case 1: Admin access granted
    if not old_user.is_staff and instance.is_staff:
        send_mail(
            subject="You have been granted admin access",
            message=f"Hello {instance.username},\n\nYour account has been updated. You now have admin access to the system.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            fail_silently=False,
        )
        print(">>> Admin access granted.")

    # Case 2: Admin access removed
    elif old_user.is_staff and not instance.is_staff:
        send_mail(
            subject="Your admin access has been removed",
            message=f"Hello {instance.username},\n\nYour account has been updated. Your admin access has been revoked.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            fail_silently=False,
        )
        print(">>> Admin access removed.")

    # Case 3: Username or Password changed
    if old_user.username != instance.username:
        changes.append("username")
    if old_user.password != instance.password:
        changes.append("password")

    if changes:
        otp = generate_otp()
        message = f"""Hello {instance.username},

This is to notify you that the following details of your account were updated: {", ".join(changes)}.

To verify the change, please use the following OTP:

OTP: {otp}

If you did not make this change, please contact support immediately.

Thank you!
"""
        send_mail(
            subject="Account Update Notification with OTP",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            fail_silently=False,
        )
        print(f">>> OTP {otp} sent for changed fields: {changes}")




def generate_otp():
    return str(random.randint(100000, 999999))