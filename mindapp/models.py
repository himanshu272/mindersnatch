from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Config(models.Model):
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return "Start and End Time"

class Player(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    current_sitn = models.IntegerField(default=1)
    score = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(
            user=instance, name=instance.username
        )

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.player.save()

class option(models.Model):
    text=models.CharField(max_length=50)
    next_sit=models.IntegerField()
    end=models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Situation(models.Model):
    situation_no= models.IntegerField(unique=True) 
    image = models.ImageField(upload_to = 'images',default='images/level1.jpg')
    # audio = models.FileField(upload_to = 'audio',default='audios/default.mp3')
    text = models.TextField()
    option_1 = models.ForeignKey(option,related_name='option1',on_delete=models.CASCADE,default=1)
    option_2 = models.ForeignKey(option,related_name='option2',on_delete=models.CASCADE,default=1)
    option_3 = models.ForeignKey(option,related_name='option3',on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.text

