from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

class Priority(models.TextChoices):
    LOW = 'Low', 'Low'
    MEDIUM = 'Medium', 'Medium'
    HIGH = 'High', 'High'

class TaskManager(models.Manager):
    def overdue(self, user):
        return self.filter(
            user=user,
            due_date__lt=timezone.now(),
            is_complete=False
        )

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )

    objects = TaskManager()

    def __str__(self):
        return f"{self.title} (due {self.due_date})"
    
@receiver(post_save, sender=Task)
def notify_due_soon(sender, instance, created, **kwargs):
    # print(f"Task {instance.title} created: {created}")
    if created:
        now_utc = timezone.now()
        due_utc = instance.due_date
        now = timezone.localtime(now_utc)
        due_date_local = timezone.localtime(due_utc)
        one_hour = now + timezone.timedelta(hours=1)
        # print(f"Current local time: {now}, One hour from now: {one_hour}, Task due date (local): {due_date_local}")
        # print(f"now tzinfo: {now.tzinfo}, due_date tzinfo: {due_date_local.tzinfo}")

        if now <= due_date_local <= one_hour:
            # print(f"Task {instance.title} is due within the next hour, sending email notification.")
            send_mail(
                subject='Task due soon!',
                message=f'Your task "{instance.title}" is due within the hour!',
                from_email='someguy@gmail.com',
                recipient_list=[instance.user.email],
                fail_silently=True,
            )
