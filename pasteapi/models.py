from django.db import models
from user.models import User
from django.db.models.signals import pre_save
from .utility import shorten




class PasteBin(models.Model):
    user = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    text = models.TextField()
    shorten_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        if not self.shorten_url:
            self.shorten_url = shorten(self)
        return super().save(*args,**kwargs)

def link_pre_save(instance,*args,**kwargs):
    if not instance.shorten_url:
        new_link = instance.shortene
        instance.shorten_url=new_link
pre_save.connect(link_pre_save,sender=PasteBin)