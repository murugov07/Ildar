from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class UserUpgrade(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Расширение пользователя'
        verbose_name_plural = 'Расширения пользователя'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserUpgrade.objects.create(user=instance)


class SupportModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    data = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.text[:100])+"..."

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'