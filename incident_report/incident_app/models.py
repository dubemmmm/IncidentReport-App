from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib import messages


# Create your models here.
User = get_user_model()
class Incident(models.Model):
    category_choices = [
        ('Accident', 'Accident'),
        ('Fighting', 'Fighting'),
        ('Rioting', 'Rioting'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, choices=category_choices)
    description = models.TextField(blank=False, max_length=400)
    address = models.CharField(max_length=255, default='')
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.category
    
# Example: Use Django messaging framework to send a message to users when a new Incident is added
'''@receiver(post_save, sender=Incident)
def send_notification_on_new_incident(sender, instance, created, **kwargs):
    if created:
        reporting_user = instance.user
        all_other_users = User.objects.exclude(pk=reporting_user.pk)

        for user in all_other_users:
            message_text = f"A new incident has been reported: {instance.category}"
            messages.success(user, message_text)'''
    
    