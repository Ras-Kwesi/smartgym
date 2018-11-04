from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model

# User = get_user_model()


# Create your models here.

# Used the Abstract user and not extend user so as to add common factors of all app user is the USER model
# Profiles for unique feature of users are going to be extended to other profile classes ud=sing one to One R/ship
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'gymnast'),
        (2, 'trainer'),
        (3, 'gym_manager'),
    )

    profile_pic = models.ImageField(upload_to='images/', blank=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,null=True,blank=True)
    # location =
    contact = models.CharField(max_length=30, blank=True)


# This is the Class for the clients and has the usique properties of gmnasts
class Gymnast(models.Model):
    user = models.ManyToManyField(User, related_name='gymnast')
    goals = (
        ('Losing weight', 'Losing weight'),
        ('Getting toned', 'Getting toned'),
        ('Getting bigger', 'Getting bigger'),
        ('Maintain fitness', 'Maintain fitness'),
    )
    weight = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    goal = models.CharField(max_length=30, choices=goals)
    contact = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=50)
    chatroom = models.ManyToManyField('Chatroom')
    gym = models.ForeignKey('Gym', null=True)


# This is the class for the Trainer and has the unique features of the Trainers
class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length =30)
    bio = models.CharField(max_length =30)
    # location= models.ForeignKey(location)
    gym = models.ForeignKey('Gym')
    specially=models.CharField(max_length =30)
    year_Experience=models.CharField(max_length =30)


# This is the class for the GymManager and Has the unque features of the Gym Manager
class GymManager(models.Model):
    user = models.OneToOneField(User, related_name='gym_manager')
    bio = models.TextField(max_length=100, blank=True)
    profilepic = models.ImageField(upload_to='picture/',blank=True)


# This is the Chatroom Model that is related to User so as any user(Gymnast/trainer..) Can create a chatroom
class Chatroom(models.Model):
    name = models.CharField(max_length=20,unique=True)
    info = models.TextField(max_length=100)
    admin = models.ForeignKey(User,related_name='administrate')
    users = models.ManyToManyField(User,related_name='chatroom')

    @classmethod
    def addchatroom(cls, chatroom, newuser):
        room, created = cls.objects.get_or_create(
            chatroom=chatroom
        )
        room.users.add(newuser)

    @classmethod
    def removechatroom(cls, chatroom, newuser):
        room, created = cls.objects.get_or_create(
            chatroom=chatroom
        )
        room.users.remove(newuser)

    def save_chatroom(self):
        self.save()

    def remove_chatroom(self):
        self.delete()

    @classmethod
    def get_chatroom(cls,id):
        room = Chatroom.objects.get(id=id)
        return room


# This is the Post model for the posts that come under the Chatroom
class Post(models.Model):
    title = models.CharField(max_length=30)
    post = models.TextField(max_length=100)
    chatroom = models.ForeignKey(Chatroom,related_name='posts', null=True)
    poster = models.ForeignKey(User, related_name='post')


    def save_post(self):
        self.save()

    def remove_post(self):
        self.delete()

    @classmethod
    def get_hood_posts(cls,id):
        posts = Post.objects.filter(id = id)
        return posts


# This is the Gym class that falls only under a gym manager, but related to it through a foreign key
class Gym(models.Model):
  '''
  Class that contains gym class properties,methods and functions
  '''
  name = models.CharField(max_length=100)
  posted_on = models.DateTimeField(auto_now_add=True)
  description = models.TextField(blank=True,null=True)
  image = models.ImageField(upload_to='images/')
  location = models.CharField(max_length=100)
  working_hours = models.TextField()
  manager = models.ForeignKey('GymManager',default = 0)


# This is the event class and is related to user as a foreign key, any user can create an event
class Event(models.Model):
  name = models.CharField(max_length=35)
  description = models.TextField(max_length=100)
  event_date = models.DateTimeField()
  admin = models.ForeignKey(User)