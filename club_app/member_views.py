#all functions of members will be defined here
from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils import timezone 
from .models import Feedback,Member,Query_Doubt,Coach


from .forms import UserQuery
from django.db.models import Q 


def member_home(request):
   if "session_key" not in request.session.keys():
      return redirect("member_login")
   
   id=request.session["session_key"]
   member_obj=Member.objects.get(member_id=id)
   context={"member_key":member_obj}
   return render(request,'club_app/member/member_dashboard.html',context)



def query_doubt(request):

   if request.method=="GET":
     if "session_key" not in request.session.keys(): 
      return redirect("member_login")
     
     user_question=UserQuery()
     context={"form":user_question}

     return render(request,"club_app/member/query_doubt.html",context)  
     

   if request.method=="POST":
        
        print("in post method")
        id=request.session["session_key"]
        user_question=UserQuery(request.POST)
        if user_question.is_valid():
         user_doubt=user_question.save(commit=False)
         user_doubt.member_id=id 
         user_doubt.save()
         messages.success(request,"Thankyou for your query we'll contact you soon")
        return redirect('query_doubt')
   
   
def view_answer(request):
   if "session_key" not in request.session.keys():
      return redirect("member_login")
   else:
      id=request.session["session_key"]
      answer_list=Query_Doubt.objects.filter(member_id=id)
      context={"answer_key":answer_list}
      return render(request,'club_app/member/view_answer.html',context)
   

def member_logout(request):
   if "session_key" not in request.session.keys():
      return redirect("member_login")
   else:
      del request.session["session_key"]
      del request.session["role"]
      return redirect("member_login")



def feedback(request):
   if request.method=="GET":
     if "session_key" not in request.session.keys():
       return redirect("member_login")
     
     return render(request,'club_app/member/feedback.html')
    

   if request.method=="POST":
         user_name=request.POST["name"]
         user_email=request.POST["email"]
         user_rating=request.POST["rating"]
         user_review=request.POST["review"]
         user_date=request.POST["date"]
         feedback_obj=Feedback(name=user_name,email=user_email,rating=user_rating,review=user_review,date=user_date)
         feedback_obj.save()
         messages.success(request,"Thanku for your valuable feedback  will consider this very soon😎😎")
         return redirect("feedback")


        
def member_login(request):

    if request.method == "GET":
        return render(request, 'club_app/member/member_login.html')

    if request.method == "POST":
        mem_id   = request.POST["id"]
        mem_pass = request.POST["password"]

        member_list = Member.objects.filter(member_id=mem_id, password=mem_pass)
        size = len(member_list)

        if size == 1:
            request.session["session_key"] = mem_id
            request.session["role"] = "Member"
            member_obj = member_list[0]
            print("COACH VALUE:", member_obj.coach)

            context = {
                "member_key": member_obj
            }
            return render(request, 'club_app/member/member_dashboard.html', context)

        else:
            messages.error(request, "Invalid user ID or password")
            return redirect("member_login")
          

def member_registration(request):
    # ── Hardcoded coach list for the registration form ──
    all_coaches = [
        {"name": "Arjun Sharma",      "sport": "Cricket"},
        {"name": "Sanjay Pandey",     "sport": "Cricket"},
        {"name": "Rohit Verma",       "sport": "Football"},
        {"name": "Priya Nair",        "sport": "Badminton"},
        {"name": "Anjali Dubey",      "sport": "Badminton"},
        {"name": "Suresh Patel",      "sport": "Basketball"},
        {"name": "Meena Rajput",      "sport": "Swimming"},
        {"name": "Pooja Saxena",      "sport": "Swimming"},
        {"name": "Vikram Singh",      "sport": "Boxing"},
        {"name": "Amit Tiwari",       "sport": "Hockey"},
        {"name": "Sneha Gupta",       "sport": "Tennis"},
        {"name": "Deepak Yadav",      "sport": "Athletics"},
        {"name": "Kavita Mishra",     "sport": "Volleyball"},
        {"name": "Rahul Chauhan",     "sport": "Table Tennis"},
        {"name": "Nikhil Srivastava", "sport": "Kabaddi"},
    ]

    if request.method == "GET":
        return render(request, 'club_app/member/member_registration.html', {'coaches': all_coaches})

    
            # In member_views.py — replace the member_registration POST block with this:

    if request.method == "POST":
        user_id               = request.POST.get("id")
        user_password         = request.POST.get("password")
        user_name             = request.POST.get("name")
        user_phone            = request.POST.get("phone")
        user_email            = request.POST.get("email")
        user_gender           = request.POST.get("gender")
        user_city             = request.POST.get("city")
        user_address          = request.POST.get("address")
        user_sports           = request.POST.getlist('sports')
        user_sports_str       = ', '.join(user_sports)
        user_pic              = request.FILES.get("profile_picture")
        coach                 = request.POST.get("selected_coach", "")
        subscription_duration = request.POST.get("subscription_duration", "")
        subscription_amount   = request.POST.get("subscription_amount", 0)

        member_reg_obj = Member(
            member_id             = user_id,
            password              = user_password,
            name                  = user_name,
            phone                 = user_phone,
            email                 = user_email,
            gender                = user_gender,
            city                  = user_city,
            address               = user_address,
            sports                = user_sports_str,
            profile_picture       = user_pic,
            coach                 = coach,
            subscription_duration = subscription_duration,
            subscription_amount   = int(subscription_amount) if subscription_amount else 0,
        )
        member_reg_obj.save()

        messages.success(request, f"Welcome {user_name}! Registration successful 🎉")
        return redirect('member_login')

               # ← goes to login, not coach_details


def member_edit_profile(request):
    if request.method == "GET":
        if "session_key" not in request.session:
            return redirect("member_login")
        id         = request.session["session_key"]
        member_obj = Member.objects.get(member_id=id)

        # Pass all coaches for the sport filter
        coaches_for_js = [
            {"name": c.name, "sport": c.area_of_intrest}
            for c in Coach.objects.all()
        ]

        context = {
            "member_key": member_obj,
            "coaches"   : coaches_for_js,
        }
        return render(request, 'club_app/member/member_edit_profile.html', context)

    if request.method == "POST":
        id = request.session["session_key"]

        update_fields = {
            "name"   : request.POST.get("name"),
            "email"  : request.POST.get("email"),
            "phone"  : request.POST.get("phone"),
            "gender" : request.POST.get("gender"),
            "city"   : request.POST.get("city"),
            "address": request.POST.get("address"),
            "sports" : ', '.join(request.POST.getlist("sports")),
            "coach"  : request.POST.get("selected_coach", ""),
        }

        new_password = request.POST.get("password", "").strip()
        if new_password:
            update_fields["password"] = new_password

        Member.objects.filter(member_id=id).update(**update_fields)

        new_pic = request.FILES.get("profile_picture")
        if new_pic:
            member_obj = Member.objects.get(member_id=id)
            member_obj.profile_picture = new_pic
            member_obj.save()

        messages.success(request, "Profile updated successfully 👍")
        return redirect('member_edit_profile')
