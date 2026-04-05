from django.contrib import admin
from .models import Event, Notice, Contact, User_detail, Member, Feedback, Coach, Query_Doubt


class Feedback_admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'rating', 'review']
    list_filter  = ('rating',)


class Contact_admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'question', 'date']


class Event_admin(admin.ModelAdmin):
    list_display = ['event_name', 'event_venue', 'event_time', 'event_organizer', 'event_description']
    list_filter  = ('event_time', 'event_venue')


class Coach_admin(admin.ModelAdmin):
    # ✅ all fields that actually exist in the merged Coach model
    list_display   = ['name', 'email', 'phone', 'city', 'area_of_intrest', 'experience']
    search_fields  = ('name', 'city', 'area_of_intrest')
    list_filter    = ('city', 'area_of_intrest')


def verify_payment(modeladmin, request, queryset):
    queryset.update(payment=True)
verify_payment.short_description = "✅ Mark payment as verified"


class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'transaction_id', 'payment', 'coach', 'sports']
    actions      = [verify_payment]


admin.site.register(Event,      Event_admin)
admin.site.register(Notice)
admin.site.register(Coach,      Coach_admin)
admin.site.register(User_detail)
admin.site.register(Contact,    Contact_admin)
admin.site.register(Feedback,   Feedback_admin)
admin.site.register(Member,     MemberAdmin)
admin.site.register(Query_Doubt)

admin.site.site_header  = "Sports Club Admin Dashboard"
admin.site.site_title   = "Sports Club Management"
admin.site.index_title  = "Manage Events, Coaches & Members Efficiently"