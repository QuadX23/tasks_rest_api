from django.db import models

from tasks.models import Task


class User(models.Model):
    name = models.CharField(max_length=32)
    position = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    is_superuser = models.BooleanField(default=False)

    tasks = models.ManyToManyField(Task, related_name='users', blank=True)
    tasks_on_review = models.ManyToManyField(Task, through='TaskReview', through_fields=('user', 'task'),
                                             related_name='reviewers', blank=True)

    def __str__(self):
        return f'{self.name} ({self.position} in {self.city})'


class TaskReview(models.Model):
    class Meta:
        unique_together = ('user', 'task', 'task_performer')

    user = models.ForeignKey(User, related_name='reviewer', on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name='review', on_delete=models.CASCADE)
    task_performer = models.ForeignKey(User, related_name='performer', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.id} {self.task.id} {self.task_performer.id}'