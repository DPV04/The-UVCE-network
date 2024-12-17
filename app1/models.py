from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(unique=True,null=True)
    bio=models.TextField(null=True)
    year=models.CharField(max_length=200,default="none",choices=[
      ('First','First'),
      ('Second','Second'),
      ('Third','Third'),
      ('Fourth','Fourth'),
     
   ])
    branch=models.CharField(max_length=200,default="none",choices=[
      ('CSE','CSE'),
      ('ISE','ISE'),
      ('AI-ML','AI-ML'),
      ('ECE','ECE'),
      ('EEE','EEE'),
      ('MECHE','MECH'),
    
   ])
    interests=models.CharField(max_length=50,null=True,default="none")
 
    avatar = models.FileField(null=True,default="none")




class Topic(models.Model):
   tname=models.CharField(max_length=200,null=True)
   def __str__(self):
        return self.tname if self.tname else "Unnamed Room"

class Room(models.Model):
    host =models.ForeignKey(User,  on_delete=models.SET_NULL, null=True)
    topicname=models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    participants=models.ManyToManyField(
       User,related_name='participants',blank=True)
    Photo=models.FileField(default='None')



    class Meta:
       ordering=['-updated','-created']

    def __str__(self):
     return self.name
    
    def __str__(self):
     return self.description[0:50]

    def __str__(self):
        return self.name if self.name else "Unnamed Room"

    
    



class Messages(models.Model):
   user=models.ForeignKey(User, on_delete=models.CASCADE)
   room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name="message")
   body= models.TextField()
   updated=models.DateTimeField(auto_now=True)
   created=models.DateTimeField(auto_now_add=True)

   class Meta:
      ordering = ['-updated', '-created']

   def __str__(self):
     return self.body[0:50]
   




   




class usercredentials(models.Model):
 name=models.ForeignKey(User,on_delete=models.CASCADE)
 year=models.CharField(max_length=20,choices=[
      ('first','first'),
      ('Second','Second'),
      ('Third','Third'),
      ('Fourth','Fourth'),
      ]) 
    
 branch=models.CharField(max_length=20,choices=[
      ('CSE','CSE'),
      ('ISE','ISE'),
      ('AI-ML','AI-ML'),
      ('ECE','ECE'),
      ('EEE','EEE'),
      ('MECHE','MECH'),
    
      ] )
 
 photo=models.FileField(default='None')
   
 interests=models.CharField(max_length=50)
 bio=models.CharField(max_length=200)



class upload(models.Model):
   name=models.ForeignKey(Room,on_delete=models.CASCADE)
   interestsname=models.CharField(max_length=200,null=True)
   image=models.FileField() 
   description=models.TextField()
   updated=models.DateTimeField(auto_now=True,)
   created=models.DateTimeField(auto_now_add=True,)

   class Meta:
      ordering = ['-updated', '-created']

   def __str__(self):
     return self.description[0:50]   
   
   def __str__(self):
     return self.interestsname