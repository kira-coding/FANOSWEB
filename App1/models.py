from django.db import models

# Create your models here.
class userOn(models.Model):
    email=models.EmailField(max_length=100,null=False,blank=False,default='')
class User(models.Model):
    nick_name=models.CharField(max_length=100,null=False,blank=False,default='')
    password=models.CharField(max_length=100,null=False,blank=False,default='')
    email=models.EmailField(max_length=100,null=False,blank=False,default='')
    tgUserName=models.CharField(max_length=100)
    phoneNumber=models.IntegerField()
    def __str__(self):
        return self.nick_name+ str(self.id)
class Topic(models.Model):
    name=models.CharField(max_length=100,)
    creator=models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.creator.nick_name

class Massage(models.Model):
    sender=models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE, null=False)
    content=models.CharField(max_length=10000,null=False)
    date=models.DateTimeField()
    def __str__(self):
        return self.sender.nick_name+':-'+self.content

