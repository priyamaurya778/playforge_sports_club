from django.urls import path 
from . import views,member_views

urlpatterns=[
    path("",views.home,name="home"),

    path("about/",views.about,name="about"), #"about/" -> End Point

    path("gallery/",views.gallery,name="gallery"),

    path("contact/",views.contact,name="contact"),

    path("feedback/",member_views.feedback,name="feedback"),

    path("member_login/",member_views.member_login,name="member_login"),

    path("cricket/",views.cricket,name="cricket"),

    path("football/",views.football,name="football"),

    path("badminton/",views.badminton,name="badminton"),

    path("basketball/",views.basketball,name="basketball"),

    path("coach/",views.coach_details,name="coach_details"),

    path("member_registration/",member_views.member_registration,name="member_registration"),

    path("reviews/",views.reviews,name="reviews"),

    path("career/",views.career,name="career"),

    path("query_doubt/",member_views.query_doubt,name="query_doubt"),

    path("member_edit_profile/",member_views.member_edit_profile,name="member_edit_profile"),

    path("member_home/",member_views.member_home,name="member_home"),

    path("member_logout/",member_views.member_logout,name="member_logout"),

    path("view_answer/",member_views.view_answer,name="view_answer"),

    path('search_results/',views.search_results, name='search_results'),  # Define the search_results URL
    





]

