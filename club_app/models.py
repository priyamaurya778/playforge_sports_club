from django.db import models
from django.utils import timezone

# Create your models here.
#event model to create event table
class Event(models.Model):
    event_name=models.CharField(max_length=55)  #class variable=event_name
    
    event_venue=models.CharField(max_length=100)   

    event_time=models.DateField(default=timezone.now)

    event_organizer=models.CharField(max_length=100,default="Elite Sports Club") 

    event_description=models.TextField()

    def __str__(self): #to represent object in the form of string
        return self.event_name 

class Notice(models.Model):
    notice_time=models.TimeField(default=timezone.now)
    notice_by=models.CharField(max_length=100,default="Elite Sports Club")
    notice_description=models.TextField()

    def __str__(self):
        return self.notice_description

#coach model
class Coach(models.Model):
    coach_id=models.CharField(max_length=50, primary_key=True)
    password=models.CharField(max_length=50)
    name=models.CharField(max_length=100,default="null")
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    city=models.CharField(max_length=20)
    address=models.TextField(max_length=100)
    sport_name=models.CharField(max_length=40,default="")
    experience=models.TextField(max_length=200)
    about_coach=models.TextField(max_length=100)
    area_of_intrest=models.TextField(max_length=100)
    coach_pic=models.FileField(max_length=100,upload_to="club_app/football_coach.jpg",default="")#upload_to ="club_app/Coach_pic.jpg" -->correction
     
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name=models.CharField(max_length=55)
    email=models.CharField(max_length=55)
    question=models.TextField()
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name=models.CharField(max_length=55)
    email=models.CharField(max_length=55)
    rating=models.CharField(max_length=10)
    review=models.TextField()
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name



gender=(('','Select Gender'),
        ("male","male"),
          ("female","female"),
)    

class Member(models.Model):
    member_id = models.CharField(max_length=45,primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=100,default="null")
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=10,choices=gender)
    city = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    date = models.DateField(default=timezone.now)
    payment=models.BooleanField(default=False)
    profile_picture=models.ImageField(upload_to="club_app/member_pictures",blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class User_detail(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    about_user=models.TextField(default="")
    user_cv=models.ImageField(upload_to='club_app/user_cv',blank=True,null=True)
    date=models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.name 
    
class Query_Doubt(models.Model):
    member_id=models.CharField(max_length=50,default="")
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    question=models.TextField(max_length=200)
    question_date=models.DateField(default=timezone.now)
    answer=models.TextField(default="")
    answer_date=models.DateField(default=None,blank=True, null=True)

    def __str__(self):
        return self.name
    

    

    
    


  

     
      
       


