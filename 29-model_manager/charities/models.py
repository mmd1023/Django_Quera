from django.db import models
from django.db.models import Q
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Benefactor(models.Model):
    class Experience(models.IntegerChoices):
        BEGINNER = 0, 'Beginner'
        INTERMEDIATE = 1, 'Intermediate'
        EXPERT = 2, 'Expert'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices=Experience.choices, default=Experience.BEGINNER)
    free_time_per_week = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(168)])

    def __str__(self):
        return f"{self.user} ({self.get_experience_display()})"


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return self.filter(charity__user=user)

    def related_tasks_to_benefactor(self, user):
        return self.filter(assigned_benefactor__user=user)

    def all_related_tasks_to_user(self, user):
        return self.filter(
            Q(charity__user=user) |
            Q(assigned_benefactor__user=user) |
            Q(state=Task.State.PENDING)
        )


class Task(models.Model):
    class State(models.TextChoices):
        PENDING = 'P', 'Pending'
        WAITING = 'W', 'Waiting'
        ASSIGNED = 'A', 'Assigned'
        DONE = 'D', 'Done'

    assigned_benefactor = models.ForeignKey(Benefactor, on_delete=models.SET_NULL, null=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(null=True, blank=True)
    age_limit_to = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    gender_limit = models.CharField(max_length=1, choices=User.Gender.choices, null=True, blank=True)
    state = models.CharField(max_length=1, choices=State.choices, default=State.PENDING)
    title = models.CharField(max_length=60)

    objects = TaskManager()

    def __str__(self):
        return f"{self.assigned_benefactor} | {self.charity} | ({self.get_state_display()})"
