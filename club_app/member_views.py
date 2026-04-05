#all functions of members will be defined here
from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils import timezone 
from .models import Feedback,Member,Query_Doubt


from .forms import UserQuery
from django.db.models import Q 


def member_home(request):
   if "session_key" not in request.session.keys():
      return redirect("member_login")
   
   id=request.session["session_key"]#fetching values from session to identify user and Identifies which user is currently logged in.
   # mem_role=request.session["role"]
   member_obj=Member.objects.get(member_id=id)#return a single obj and if not matched raise an error
   #member_obj = Member.objects.filter(member_id=id).first() # Returns None if no match
   #Fetches member details from the database for display on the dashboard
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
        user_question=UserQuery(request.POST)#,request.FILES)
        if user_question.is_valid():
         user_doubt=user_question.save(commit=False) #data abhi save nhi hoga just put it on hold
         user_doubt.member_id=id 
         user_doubt.save()
         # user_question.save()
         messages.success(request,"Thankyou for your query we'll contact you soon")
        return redirect('query_doubt')
   
   
def view_answer(request):
   if "session_key" not in request.session.keys():
      return redirect("member_login")
   else:
      id=request.session["session_key"]
      answer_list=Query_Doubt.objects.filter(member_id=id) #all questions came in form of list
      context={"answer_key":answer_list}
      return render(request,'club_app/member/view_answer.html',context)
   

def member_logout(request):
   if "session_key" not in request.session.keys():
      return redirect("member_login")
   else:
      del request.session["session_key"] #it only removes one key (session_key), not the whole session
      del request.session["role"] # request.session.flush()  # Clears the entire session
      return redirect("member_login")



def feedback(request):
   if request.method=="GET": #http protocol sends user data using POST method 
     if "session_key" not in request.session.keys():
       return redirect("member_login")
     
     return render(request,'club_app/member/feedback.html')
    

   if request.method=="POST":
         
         #store data in feedback table and send message to feedback.html
     
         user_name=request.POST["name"]#request.POST[]built-in dictionary 
         user_email=request.POST["email"]
         #Sports=request.POST["sports"]
         user_rating=request.POST["rating"]
         user_review=request.POST["review"]
         user_date=request.POST["date"]
         #print(user_name,user_email,user_rating,user_rewiew)
         feedback_obj=Feedback(name=user_name,email=user_email,rating=user_rating,review=user_review,date=user_date)#creating Contact class object
         feedback_obj.save()#ORM map with Feedback table fields
         messages.success(request,"Thanku for your valuable feedback  will consider this very soon😎😎")
    #return render(request,'club_app/html/index.html')
         return redirect("feedback")#it is logical name of the view


def member_login(request):
    
    if request.method=="GET":
     return render(request,'club_app/member/member_login.html')
    
    if request.method=="POST":
       mem_id=request.POST["id"]
       mem_pass=request.POST["password"]  

      #  member_list=Member.objects.filter(member_id=mem_id,password=mem_pass,payment=True)
       member_list=Member.objects.filter(Q(member_id=mem_id)& Q(password=mem_pass) &Q(payment=True))
       size=len(member_list)
       print("size is",size)#if member_list.exists():


    if size==1:
          request.session["session_key"]=mem_id #binding member id in session with key member_key
          request.session["role"]="Member"
          member_obj=member_list[0] #fetching the single obj from the list and storing in member_obj
         #  print(member_obj.name) #it will print name of memeber
         #  print(type(member_obj))#will return class name of memberobject
          
          context={
             "member_key":member_obj
          }
          return render(request,'club_app/member/member_dashboard.html',context)


    else:
          messages.error(request,"Invalid user id and password or Your fees has been not deposited")#message.error is predifined tag
          return redirect("member_login")
       
          

def member_registration(request):
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

    if request.method == "POST":
        user_id         = request.POST["id"]
        user_password   = request.POST["password"]
        user_name       = request.POST["name"]
        user_phone      = request.POST["phone"]
        user_email      = request.POST["email"]
        user_gender     = request.POST["gender"]
        user_city       = request.POST["city"]
        user_address    = request.POST["address"]
        user_sports     = request.POST.getlist('sports')
        user_sports_str = ', '.join(user_sports)
        user_pic        = request.FILES["profile_picture"]
        transaction     = request.POST.get("transaction_id", "")

        member_reg_obj = Member(
            member_id=user_id,
            password=user_password,
            name=user_name,
            phone=user_phone,
            email=user_email,
            gender=user_gender,
            city=user_city,
            address=user_address,
            sports=user_sports_str,
            profile_picture=user_pic,
        )
        member_reg_obj.save()

        # ✅ Save sports to session for coach filtering
        request.session['member_sports'] = user_sports
        request.session['member_id']     = user_id       # save id for coach assignment later
        request.session.modified = True

        messages.success(request, "Thanku for Registration now you are our member😎😎")
        return redirect('coach_details')

        

        
        

def member_edit_profile(request):
   if request.method=="GET" :
     if "session_key" not in request.session.keys(): 
      return redirect("member_login")
     else:
          id=request.session["session_key"]
          member_obj=Member.objects.get(member_id=id) #return a single object
          context={"member_key": member_obj}
         
          return render(request,'club_app/member/member_edit_profile.html',context)
     
   if request.method=="POST":
         
         user_email=request.POST["email"]#user_email(obj) me email ki new data feed ho rhi hai -> jisase further pass ho jaye
         user_phone=request.POST["phone"]
         user_city=request.POST["city"]
         user_address=request.POST["address"]
   #existing obj me new value ko save/update kr rhe hai
         id=request.session["session_key"] #user ki session se id mil gai
         Member.objects.filter(member_id=id).update( 
            email=user_email,
            phone=user_phone,
            city=user_city,
            address=user_address
         )
         
         messages.success(request,"Profile updated sucessfully👍")
         return redirect('member_edit_profile') 



         # member_obj=Member.objects.get(member_id=id) #member class-> member_id(primary key) and instantiate the class(Member) 
         # member_obj.email=user_email #email-> is model name || user_email-> is new obj
         # member_obj.phone=user_phone
         # member_obj.city=user_city
         # member_obj.address=user_address
         # member_obj.save()   #save/update all new values in existing row/models 
         # status=member_obj.update(email=user_email,phone=user_phone,city=user_city,address=user_address)
         # print(status)
        # return redirect('member_home')
      
        
              
        

        
         
   
   
      
           









