from django.contrib import admin
from .models import Event , Notice , Contact ,User_detail ,Member,Feedback,Coach,Query_Doubt   # .models -> same directory (event and notice are two models)


# Register your models here.


class Feedback_admin(admin.ModelAdmin):
    list_display=['name','email','rating','review']
    list_filter=('rating',)

class Contact_admin(admin.ModelAdmin):
    list_display=['name','email','question','date']

class Event_admin(admin.ModelAdmin):
    list_display=['event_name','event_venue','event_time','event_organizer','event_description']
    list_filter=('event_time','event_venue')

class Coach_admin(admin.ModelAdmin):
    list_display=['name','email','phone','city','address','experience']
    search_fields=('city','experience')
    list_filter=('experience',)


admin.site.register(Event,Event_admin) #to show/register the admin model in admin interface
admin.site.register(Notice) # new model to show admin
admin.site.register(Coach,Coach_admin)
admin.site.register(User_detail)
admin.site.register(Contact,Contact_admin)
admin.site.register(Feedback,Feedback_admin)
admin.site.register(Member) 
admin.site.register(Query_Doubt)
# admin.site.register(Edit_Profile)


# Admin site customizations
admin.site.site_header = "Sports Club Admin Dashboard"
admin.site.site_title = "Sports Club Management"
admin.site.index_title = "Manage Events, Coaches & Members Efficiently"


