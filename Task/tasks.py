
from django.db.models.signals import post_save
from django.dispatch import receiver
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .models import Task

@receiver(post_save, sender=Task)
def send_task_creation_notification(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'New Task Created',
            f'The task "{instance.name}" has been created with a deadline of {instance.deadline}.',
            'vasundhara.2510@example.com',
            [instance.user.email],  # Use the user foreign key
        )


@shared_task
def check_task_deadlines():
    now = timezone.now()
    # Check for tasks that are due within the next day
    upcoming_tasks = Task.objects.filter(deadline__lte=now + timedelta(days=1))

    for task in upcoming_tasks:
        if task.deadline <= now:
            # Task deadline has passed
            subject = 'Task Deadline Passed'
            message = f'The deadline for the task "{task.name}" has passed!'
        else:
            # Task deadline is approaching
            subject = 'Task Deadline Reminder'
            message = f'The deadline for the task "{task.name}" is approaching!'

        send_mail(
            subject,
            message,
            'support@taskmanager.com',
            [task.user.email],  # Using user_id to get the email
        )