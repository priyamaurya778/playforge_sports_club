from django.shortcuts import render,HttpResponse,redirect
from .models import Notice,Event,Contact,Coach,Feedback ,Member
from django.contrib import messages
from .forms import UserForm
from django.db.models import Q 

# Create your views here.
def home(request):
    #return HttpResponse("<h1>This is Home Page of Sports Club</h1>")
     notice_list=Notice.objects.all() #select * from Notice
     #print(type(notice_list)) # class Queryset[noticeobj1,noticeobj2,noticeobj3]
     #print(notice_list)
     event_list=Event.objects.all()
     context={
         "notice_key":notice_list, #dictionary
         "event_key":event_list,   

        }
     

     return render(request,'club_app/html/index.html',context)  #    
    

def about(request):
    #return HttpResponse("This is about us page of sports club--")
     return render(request,'club_app/html/about_us.html')

def gallery(request):
    
     return render(request,'club_app/html/gallery.html')


def contact(request):
  
    if request.method=="POST":#http protocol sends user data using POST method
         user_name=request.POST["name"]#request.POST[]built-in dictionary 
         user_email  =request.POST["email"]
        #  user_phone=request.POST.get("phone")
         user_question=request.POST["question"]
         #print(user_name,user_email,user_phone,user_question)
         contact_obj=Contact(name=user_name,email=user_email,question=user_question)#creating Contact class object
         contact_obj.save()#ORM map with contact table fields
         messages.success(request,"❤❤Thanku for contacting us We will reach you soon😎😎😎😎😎😎")
    #return render(request,'club_app/html/index.html')
         return redirect("home")#it is logical name of the view

def cricket(request):
    
    return render(request,'club_app/html/cricket.html')

def football(request):
    return render(request,'club_app/html/football.html')

def badminton(request):
    return render(request,'club_app/html/badminton.html')

def basketball(request):
    return render(request,'club_app/html/basketball.html')


def coach_details(request): #about coaches
   # if request.method=="GET": by default get function hoga
   coach_list=Coach.objects.order_by('name') #[:2] used to limit the coach details
   #coach_list=Coach.objects.raw("select * from club_app_Coach order by name")#raw SQL command
   context={"coach_key" : coach_list}
   return render(request,"club_app/html/coach_details.html",context)

def reviews(request): #about coaches
   # if request.method=="GET": by default get function hoga
   feedback_list=Feedback.objects.order_by('name')[:4] #used to limit the coach details

   context={"review_key" : feedback_list}

   return render(request,"club_app/html/reviews.html",context)

def career(request):
    if request.method=="GET":

        user_forms=UserForm()
        context={"form":user_forms} #bind object of UserForm
        #"form"-> is key
        #user

        return render(request,"club_app/html/career.html",context) #pass dict context to html page
    
    if request.method=="POST":
        user_forms=UserForm(request.POST,request.FILES)
        if user_forms.is_valid():
            user_forms.save()
            messages.success(request,"Thankyou for applying we will contact you soon🙏")
            return redirect('career') 

def search_results(request): 
    query = request.GET.get('q', '').strip()  # Get search input, remove extra spaces
    results = {}  # Dictionary to store search results from different models

    if query:
        # Search in Coach model
        coach_results = Coach.objects.filter(Q(name__icontains=query) | Q(city__icontains=query))
        if coach_results.exists():
            results['coach'] = coach_results  # Store results under 'coach' key

        # Search in Member model
        member_results = Member.objects.filter(Q(name__icontains=query) | Q(email__icontains=query) | Q(city__icontains=query))
        if member_results.exists():
            results['members'] = member_results  # Store results under 'members' key
            

        # Search in Event model
        event_results = Event.objects.filter(Q(event_name__icontains=query) | Q( event_description__icontains=query) | Q( event_venue__icontains=query))
        if event_results.exists():
            results['events'] = event_results  # Store results under 'events' key
        
        #search in Feedback model
        feedback_results = Feedback.objects.filter(Q(review__icontains=query) | Q(rating__icontains=query) |Q(name__icontains=query))
        if feedback_results.exists():
            results['feedbacks'] = feedback_results    # Store results under 'feedbacks' key 
  

    return render(request, 'club_app/html/search_results.html', {'query': query, 'results': results})