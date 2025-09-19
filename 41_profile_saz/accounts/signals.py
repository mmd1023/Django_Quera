from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from django.contrib.auth import get_user_model
from .models import Profile, Website

User = get_user_model()


@receiver(post_save, sender=User)
def tell_people(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(m2m_changed, sender=Website.users.through)
def do_something(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action not in ['post_add', 'post_remove', 'post_clear']:
        return

    if reverse:
        # user changed
        user = instance
        bio = '\n'.join([w.url for w in user.website_set.all().order_by('url')])
        user.profile.bio = bio
        user.profile.save()
    else:
        # website changed
        users = User.objects.filter(pk__in=pk_set)
        for user in users:
            bio = '\n'.join([w.url for w in user.website_set.all().order_by('url')])
            user.profile.bio = bio
            user.profile.save()
