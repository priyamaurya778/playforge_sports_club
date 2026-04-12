from django.db import models
from django.utils import timezone


class Event(models.Model):
    event_name        = models.CharField(max_length=55)
    event_venue       = models.CharField(max_length=100)
    event_time        = models.DateField(default=timezone.now)
    event_organizer   = models.CharField(max_length=100, default="Elite Sports Club")
    event_description = models.TextField()

    def __str__(self):
        return self.event_name


class Notice(models.Model):
    notice_time        = models.TimeField(default=timezone.now)
    notice_by          = models.CharField(max_length=100, default="Elite Sports Club")
    notice_description = models.TextField()

    def __str__(self):
        return self.notice_description


class Coach(models.Model):
    coach_id        = models.CharField(max_length=50, primary_key=True)
    password        = models.CharField(max_length=50)
    name            = models.CharField(max_length=100, default="")
    phone           = models.CharField(max_length=10)
    email           = models.CharField(max_length=100)
    gender          = models.CharField(max_length=10)
    city            = models.CharField(max_length=20)
    address         = models.TextField(max_length=100)
    sport_name      = models.CharField(max_length=40, default="")
    experience      = models.TextField(max_length=200)
    about_coach     = models.TextField(max_length=100)
    area_of_intrest = models.TextField(max_length=100)
    coach_pic       = models.ImageField(upload_to="coach_pics/", default="")

    def __str__(self):
        return self.name


class Contact(models.Model):
    name     = models.CharField(max_length=55)
    email    = models.CharField(max_length=55)
    question = models.TextField()
    date     = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name   = models.CharField(max_length=55)
    email  = models.CharField(max_length=55)
    rating = models.CharField(max_length=10)
    review = models.TextField()
    date   = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


gender = (
    ('',       'Select Gender'),
    ('male',   'male'),
    ('female', 'female'),
)

DURATION_CHOICES = (
    ('1 Month',  '1 Month'),
    ('3 Months', '3 Months'),
    ('6 Months', '6 Months'),
    ('1 Year',   '1 Year'),
)


class Member(models.Model):
    member_id             = models.CharField(max_length=45, primary_key=True)
    password              = models.CharField(max_length=50)
    name                  = models.CharField(max_length=100, default="null")
    phone                 = models.CharField(max_length=10)
    email                 = models.CharField(max_length=100)
    gender                = models.CharField(max_length=10, choices=gender)
    city                  = models.CharField(max_length=20)
    address               = models.TextField(max_length=100)
    coach                 = models.CharField(max_length=100, blank=True, null=True)
    date                  = models.DateField(default=timezone.now)
    payment               = models.BooleanField(default=False)
    sports                = models.CharField(max_length=200, blank=True, null=True)
    profile_picture       = models.ImageField(upload_to="club_app/member_pictures", blank=True, null=True)
    transaction_id        = models.CharField(max_length=100, blank=True, null=True)
    # ── NEW subscription fields ──
    subscription_duration = models.CharField(max_length=20, choices=DURATION_CHOICES, blank=True, null=True)
    subscription_amount   = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class User_detail(models.Model):
    name       = models.CharField(max_length=100)
    phone      = models.CharField(max_length=10)
    email      = models.CharField(max_length=100)
    about_user = models.TextField(default="")
    user_cv    = models.ImageField(upload_to='club_app/user_cv', blank=True, null=True)
    date       = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class Query_Doubt(models.Model):
    member_id     = models.CharField(max_length=50, default="")
    name          = models.CharField(max_length=100)
    subject       = models.CharField(max_length=100)
    email         = models.EmailField(max_length=100)
    question      = models.TextField(max_length=200)
    question_date = models.DateField(default=timezone.now)
    answer        = models.TextField(default="")
    answer_date   = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    coach_id   = models.CharField(max_length=50)
    coach_name = models.CharField(max_length=100)
    title      = models.CharField(max_length=150)
    sport      = models.CharField(max_length=100)
    date       = models.DateField()
    time       = models.TimeField()
    duration   = models.CharField(max_length=50, default="1 Hour")
    location   = models.CharField(max_length=150, default="Club Ground")
    notes      = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} — {self.coach_name}"


class Announcement(models.Model):
    coach_id   = models.CharField(max_length=50)
    coach_name = models.CharField(max_length=100)
    sport      = models.CharField(max_length=100)
    title      = models.CharField(max_length=200)
    body       = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} — {self.coach_name}"
