from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import asyncio
from .notification import send_telegram_notification

# Create your models here.


class Modal(models.Model):

    name = models.CharField(max_length=50, verbose_name="Name")
    phone = models.CharField(max_length=50, verbose_name="Phone number")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.name} {self.phone}, {self.email}"

@receiver(post_save, sender=Modal)
def notify_on_save(sender, instance, created, **kwargs):
    if created:  # Отправляем уведомление только при создании
        message = f"New client: {instance.name}\nPhone: {instance.phone}\nEmail: {instance.email}"
        
        # Запускаем асинхронную отправку сообщения
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_telegram_notification(message))
        loop.close()