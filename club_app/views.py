from django.shortcuts import render, HttpResponse, redirect
from .models import Notice, Event, Contact, Coach, Feedback, Member
from django.contrib import messages
from .forms import UserForm
from django.db.models import Q


def home(request):
    notice_list = Notice.objects.all()
    event_list  = Event.objects.all()
    context = {
        "notice_key": notice_list,
        "event_key":  event_list,
    }
    return render(request, 'club_app/html/index.html', context)


def about(request):
    return render(request, 'club_app/html/about_us.html')


def gallery(request):
    return render(request, 'club_app/html/gallery.html')


def contact(request):
    if request.method == "POST":
        user_name     = request.POST["name"]
        user_email    = request.POST["email"]
        user_question = request.POST["question"]
        contact_obj   = Contact(name=user_name, email=user_email, question=user_question)
        contact_obj.save()
        messages.success(request, "❤❤Thanku for contacting us We will reach you soon😎😎😎😎😎😎")
        return redirect("home")


def cricket(request):
    return render(request, 'club_app/html/cricket.html')

def football(request):
    return render(request, 'club_app/html/football.html')

def badminton(request):
    return render(request, 'club_app/html/badminton.html')

def basketball(request):
    return render(request, 'club_app/html/basketball.html')

def tennis(request):
    return render(request, 'club_app/html/tennis.html')

def swimming(request):
    return render(request, 'club_app/html/swimming.html')

def volleyball(request):
    return render(request, 'club_app/html/volleyball.html')

def hockey(request):
    return render(request, 'club_app/html/hockey.html')

def kabaddi(request):
    return render(request, 'club_app/html/kabaddi.html')

def athletics(request):
    return render(request, 'club_app/html/atheletics.html')


def member_registration(request):
    # ── Pull coach names from DB for live filter on registration form ──
    all_coaches    = list(Coach.objects.values('name', 'area_of_intrest'))
    coaches_for_js = [
        {"name": c["name"], "sport": c["area_of_intrest"]}
        for c in all_coaches
    ]

    if request.method == "POST":
        member_id   = request.POST.get("id")
        password    = request.POST.get("password")
        name        = request.POST.get("name")
        phone       = request.POST.get("phone")
        email       = request.POST.get("email")
        gender      = request.POST.get("gender")
        city        = request.POST.get("city")
        address     = request.POST.get("address")
        sports      = request.POST.getlist("sports")
        profile_pic = request.FILES.get("profile_picture")
        transaction = request.POST.get("transaction_id")

        member_obj = Member(
            member_id       = member_id,
            password        = password,
            name            = name,
            phone           = phone,
            email           = email,
            gender          = gender,
            city            = city,
            address         = address,
            sports          = ', '.join(sports),
            profile_picture = profile_pic,
            transaction_id  = transaction,
        )
        member_obj.save()

        request.session['member_sports'] = sports
        request.session['member_id']     = member_id
        request.session.modified         = True

        messages.success(request, f"Welcome {name}! Registration successful 🎉")
        return redirect('coach_details')

    return render(request, 'club_app/html/member_registration.html', {
        'coaches': coaches_for_js
    })


def coach_details(request):

    # ── Always ensure hardcoded coaches exist in DB ──
    hardcoded = [
        {"coach_id": "C001", "name": "Arjun Sharma",      "email": "arjun.sharma@sportsclub.in",  "phone": "9876543201", "city": "Lucknow",   "experience": "12 Years", "area_of_intrest": "Cricket",      "gender": "male",   "address": "Lucknow, UP",   "about_coach": "Expert cricket coach",  "password": "coach123"},
        {"coach_id": "C002", "name": "Rohit Verma",       "email": "rohit.verma@sportsclub.in",   "phone": "9876543202", "city": "Kanpur",    "experience": "9 Years",  "area_of_intrest": "Football",     "gender": "male",   "address": "Kanpur, UP",    "about_coach": "Football specialist",   "password": "coach123"},
        {"coach_id": "C003", "name": "Priya Nair",        "email": "priya.nair@sportsclub.in",    "phone": "9876543203", "city": "Varanasi",  "experience": "7 Years",  "area_of_intrest": "Badminton",    "gender": "female", "address": "Varanasi, UP",  "about_coach": "Badminton coach",       "password": "coach123"},
        {"coach_id": "C004", "name": "Suresh Patel",      "email": "suresh.patel@sportsclub.in",  "phone": "9876543204", "city": "Gorakhpur", "experience": "15 Years", "area_of_intrest": "Basketball",   "gender": "male",   "address": "Gorakhpur, UP", "about_coach": "Basketball expert",     "password": "coach123"},
        {"coach_id": "C005", "name": "Meena Rajput",      "email": "meena.rajput@sportsclub.in",  "phone": "9876543205", "city": "Lucknow",   "experience": "10 Years", "area_of_intrest": "Swimming",     "gender": "female", "address": "Lucknow, UP",   "about_coach": "Swimming coach",        "password": "coach123"},
        {"coach_id": "C006", "name": "Vikram Singh",      "email": "vikram.singh@sportsclub.in",  "phone": "9876543206", "city": "Hardoi",    "experience": "11 Years", "area_of_intrest": "Boxing",       "gender": "male",   "address": "Hardoi, UP",    "about_coach": "Boxing trainer",        "password": "coach123"},
        {"coach_id": "C007", "name": "Amit Tiwari",       "email": "amit.tiwari@sportsclub.in",   "phone": "9876543207", "city": "Kanpur",    "experience": "8 Years",  "area_of_intrest": "Hockey",       "gender": "male",   "address": "Kanpur, UP",    "about_coach": "Hockey specialist",     "password": "coach123"},
        {"coach_id": "C008", "name": "Sneha Gupta",       "email": "sneha.gupta@sportsclub.in",   "phone": "9876543208", "city": "Varanasi",  "experience": "6 Years",  "area_of_intrest": "Tennis",       "gender": "female", "address": "Varanasi, UP",  "about_coach": "Tennis coach",          "password": "coach123"},
        {"coach_id": "C009", "name": "Deepak Yadav",      "email": "deepak.yadav@sportsclub.in",  "phone": "9876543209", "city": "Lucknow",   "experience": "14 Years", "area_of_intrest": "Athletics",    "gender": "male",   "address": "Lucknow, UP",   "about_coach": "Athletics trainer",     "password": "coach123"},
        {"coach_id": "C010", "name": "Kavita Mishra",     "email": "kavita.mishra@sportsclub.in", "phone": "9876543210", "city": "Gorakhpur", "experience": "5 Years",  "area_of_intrest": "Volleyball",   "gender": "female", "address": "Gorakhpur, UP", "about_coach": "Volleyball coach",      "password": "coach123"},
        {"coach_id": "C011", "name": "Rahul Chauhan",     "email": "rahul.chauhan@sportsclub.in", "phone": "9876543211", "city": "Lucknow",   "experience": "13 Years", "area_of_intrest": "Table Tennis", "gender": "male",   "address": "Lucknow, UP",   "about_coach": "Table Tennis expert",   "password": "coach123"},
        {"coach_id": "C012", "name": "Nikhil Srivastava", "email": "nikhil.sri@sportsclub.in",    "phone": "9876543212", "city": "Kanpur",    "experience": "10 Years", "area_of_intrest": "Kabaddi",      "gender": "male",   "address": "Kanpur, UP",    "about_coach": "Kabaddi coach",         "password": "coach123"},
        {"coach_id": "C013", "name": "Anjali Dubey",      "email": "anjali.dubey@sportsclub.in",  "phone": "9876543213", "city": "Varanasi",  "experience": "8 Years",  "area_of_intrest": "Badminton",    "gender": "female", "address": "Varanasi, UP",  "about_coach": "Badminton trainer",     "password": "coach123"},
        {"coach_id": "C014", "name": "Sanjay Pandey",     "email": "sanjay.pandey@sportsclub.in", "phone": "9876543214", "city": "Hardoi",    "experience": "16 Years", "area_of_intrest": "Cricket",      "gender": "male",   "address": "Hardoi, UP",    "about_coach": "Senior cricket coach",  "password": "coach123"},
        {"coach_id": "C015", "name": "Pooja Saxena",      "email": "pooja.saxena@sportsclub.in",  "phone": "9876543215", "city": "Lucknow",   "experience": "7 Years",  "area_of_intrest": "Swimming",     "gender": "female", "address": "Lucknow, UP",   "about_coach": "Swimming specialist",   "password": "coach123"},
    ]

    # ✅ get_or_create runs every time — adds hardcoded if missing, skips if already exists
    # ✅ newly registered coaches (C016, C017...) are NOT affected since their coach_id won't match
    for c in hardcoded:
        Coach.objects.get_or_create(coach_id=c["coach_id"], defaults=c)

    # ── Handle coach selection POST ──
    if request.method == "POST":
        selected_coach = request.POST.get("selected_coach")
        member_id      = request.session.get("member_id")
        if selected_coach and member_id:
            Member.objects.filter(member_id=member_id).update(coach=selected_coach)
            messages.success(request, f"✅ Coach {selected_coach} assigned successfully!")
        return redirect('member_login')

    # ── GET: fetch ALL coaches from DB (hardcoded + newly registered) ──
    member_sports = request.session.get('member_sports', [])

    if member_sports:
        coach_list = Coach.objects.filter(area_of_intrest__in=member_sports)
    else:
        coach_list = Coach.objects.all()   # ✅ shows everyone

    filtered_coaches = [
        {
            "name"      : c.name,
            "email"     : c.email,
            "city"      : c.city,
            "experience": c.experience,
            "sport"     : c.area_of_intrest,
            "pic"       : f"/media/{c.coach_pic}" if c.coach_pic else f"https://randomuser.me/api/portraits/{'men' if c.gender == 'male' else 'women'}/{abs(hash(c.name)) % 99}.jpg",
        }
        for c in coach_list
    ]

    context = {
        "coach_key"    : filtered_coaches,
        "member_sports": member_sports,
    }
    return render(request, "club_app/html/coach_details.html", context)


def coach_career(request):
    if request.method == "GET":
        # ✅ render the coach registration template, NOT career.html
        return render(request, 'club_app/html/coach_career.html')

    if request.method == "POST":
        coach_obj = Coach(
            coach_id        = request.POST.get('coach_id'),
            password        = request.POST.get('password'),
            name            = request.POST.get('name'),
            phone           = request.POST.get('phone'),
            email           = request.POST.get('email'),
            gender          = request.POST.get('gender'),
            city            = request.POST.get('city'),
            address         = request.POST.get('address'),
            area_of_intrest = request.POST.get('area_of_intrest'),
            experience      = request.POST.get('experience'),
            about_coach     = request.POST.get('about_coach', ''),
            coach_pic       = request.FILES.get('coach_pic'),
        )
        coach_obj.save()
        messages.success(request, "🎉 Coach registered successfully! Your profile is now live.")
        return redirect('coach_career')


def reviews(request):
    feedback_list = Feedback.objects.order_by('name')[:4]
    context = {"review_key": feedback_list}
    return render(request, "club_app/html/reviews.html", context)


def career(request):
    # ── This is for User/Staff job applications (UserForm), NOT coaches ──
    if request.method == "GET":
        user_forms = UserForm()
        context    = {"form": user_forms}
        return render(request, "club_app/html/career.html", context)

    if request.method == "POST":
        user_forms = UserForm(request.POST, request.FILES)
        if user_forms.is_valid():
            user_forms.save()
            messages.success(request, "Thankyou for applying we will contact you soon🙏")
            return redirect('career')


def search_results(request):
    query   = request.GET.get('q', '').strip()
    results = {}

    if query:
        coach_results = Coach.objects.filter(
            Q(name__icontains=query) | Q(city__icontains=query) | Q(area_of_intrest__icontains=query)
        )
        if coach_results.exists():
            results['coach'] = coach_results

        member_results = Member.objects.filter(
            Q(name__icontains=query) | Q(email__icontains=query) | Q(city__icontains=query)
        )
        if member_results.exists():
            results['members'] = member_results

        event_results = Event.objects.filter(
            Q(event_name__icontains=query) | Q(event_description__icontains=query) | Q(event_venue__icontains=query)
        )
        if event_results.exists():
            results['events'] = event_results

        feedback_results = Feedback.objects.filter(
            Q(review__icontains=query) | Q(rating__icontains=query) | Q(name__icontains=query)
        )
        if feedback_results.exists():
            results['feedbacks'] = feedback_results

    return render(request, 'club_app/html/search_results.html', {'query': query, 'results': results})