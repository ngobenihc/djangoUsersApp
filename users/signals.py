from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch.dispatcher import receiver

from users.models import Profile


@receiver(post_save,sender =User)
def creter_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)


@receiver(pre_save,sender=User)
def generate_username(sender,instance,**kwargs):
    if not instance.username:
        username = f"{instance.first_name}_{instance.last_name}".lower()
        conuter = 1
        while User.objects.filter(username = username):
            username = f"{instance.first_name}_{instance.last_name}".lower()
            conuter ++1

        instance.username = username

