from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Coach, Member, Query_Doubt, Session, Announcement


def get_coach(request):
    coach_id = request.session.get("coach_session")
    if not coach_id:
        return None
    try:
        return Coach.objects.get(coach_id=coach_id)
    except Coach.DoesNotExist:
        return None


def coach_login(request):
    if request.method == "GET":
        return render(request, 'club_app/coach/coach_login.html')
    if request.method == "POST":
        coach_id = request.POST.get("coach_id", "").strip()
        password = request.POST.get("password", "").strip()
        try:
            coach = Coach.objects.get(coach_id=coach_id, password=password)
            request.session["coach_session"] = coach_id
            request.session["role"] = "Coach"
            return redirect("coach_dashboard")
        except Coach.DoesNotExist:
            messages.error(request, "Invalid Coach ID or Password")
            return redirect("coach_login")


def coach_dashboard(request):
    coach = get_coach(request)
    if not coach:
        return redirect("coach_login")
    members = Member.objects.filter(coach=coach.name)
    context = {"coach": coach, "members": members}
    return render(request, 'club_app/coach/coach_dashboard.html', context)


def coach_logout(request):
    request.session.pop("coach_session", None)
    request.session.pop("role", None)
    return redirect("coach_login")


def coach_edit_profile(request):
    coach = get_coach(request)
    if not coach:
        return redirect("coach_login")
    if request.method == "POST":
        coach.email       = request.POST.get("email", coach.email)
        coach.phone       = request.POST.get("phone", coach.phone)
        coach.city        = request.POST.get("city", coach.city)
        coach.address     = request.POST.get("address", coach.address)
        coach.about_coach = request.POST.get("about_coach", coach.about_coach)
        coach.experience  = request.POST.get("experience", coach.experience)
        if request.FILES.get("coach_pic"):
            coach.coach_pic = request.FILES["coach_pic"]
        coach.save()
        messages.success(request, "✅ Profile updated successfully!")
        return redirect("coach_edit_profile")
    return render(request, 'club_app/coach/coach_edit_profile.html', {"coach": coach})


def coach_member_detail(request, member_id):
    coach = get_coach(request)
    if not coach:
        return redirect("coach_login")
    try:
        member = Member.objects.get(member_id=member_id, coach=coach.name)
    except Member.DoesNotExist:
        messages.error(request, "Member not found.")
        return redirect("coach_dashboard")
    context = {"coach": coach, "member": member}
    return render(request, 'club_app/coach/coach_member_detail.html', context)


def coach_message_board(request):
    coach = get_coach(request)
    if not coach:
        return redirect("coach_login")
    assigned_ids = Member.objects.filter(coach=coach.name).values_list('member_id', flat=True)
    queries      = Query_Doubt.objects.filter(member_id__in=assigned_ids).order_by('-question_date')
    if request.method == "POST":
        query_id = request.POST.get("query_id")
        answer   = request.POST.get("answer", "").strip()
        if query_id and answer:
            try:
                q             = Query_Doubt.objects.get(id=query_id)
                q.answer      = answer
                q.answer_date = timezone.now().date()
                q.save()
                messages.success(request, "✅ Answer submitted!")
            except Query_Doubt.DoesNotExist:
                pass
        return redirect("coach_message_board")
    context = {"coach": coach, "queries": queries}
    return render(request, 'club_app/coach/coach_message_board.html', context)


def coach_session_planner(request):
    coach = get_coach(request)
    if not coach:
        return redirect("coach_login")
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "add":
            Session.objects.create(
                coach_id   = coach.coach_id,
                coach_name = coach.name,
                title      = request.POST.get("title", ""),
                sport      = coach.area_of_intrest,
                date       = request.POST.get("date"),
                time       = request.POST.get("time"),
                duration   = request.POST.get("duration", "1 Hour"),
                location   = request.POST.get("location", "Club Ground"),
                notes      = request.POST.get("notes", ""),
            )
            messages.success(request, "✅ Session added!")
        elif action == "delete":
            Session.objects.filter(id=request.POST.get("session_id"), coach_id=coach.coach_id).delete()
            messages.success(request, "🗑 Session deleted.")
        return redirect("coach_session_planner")
    sessions = Session.objects.filter(coach_id=coach.coach_id).order_by('date', 'time')
    context  = {"coach": coach, "sessions": sessions}
    return render(request, 'club_app/coach/coach_session_planner.html', context)


def coach_announcements(request):
    coach = get_coach(request)
    if not coach:
        return redirect("coach_login")
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "add":
            Announcement.objects.create(
                coach_id   = coach.coach_id,
                coach_name = coach.name,
                sport      = coach.area_of_intrest,
                title      = request.POST.get("title", ""),
                body       = request.POST.get("body", ""),
            )
            messages.success(request, "📢 Announcement posted!")
        elif action == "delete":
            Announcement.objects.filter(id=request.POST.get("ann_id"), coach_id=coach.coach_id).delete()
            messages.success(request, "🗑 Announcement deleted.")
        return redirect("coach_announcements")
    announcements = Announcement.objects.filter(coach_id=coach.coach_id).order_by('-created_at')
    context       = {"coach": coach, "announcements": announcements}
    return render(request, 'club_app/coach/coach_announcements.html', context)


def member_sessions(request):
    if "session_key" not in request.session:
        return redirect("member_login")
    member_id = request.session["session_key"]
    member    = Member.objects.get(member_id=member_id)
    try:
        coach         = Coach.objects.get(name=member.coach)
        sessions      = Session.objects.filter(coach_id=coach.coach_id).order_by('date', 'time')
        announcements = Announcement.objects.filter(coach_id=coach.coach_id).order_by('-created_at')
    except Coach.DoesNotExist:
        sessions      = []
        announcements = []
    context = {"member": member, "sessions": sessions, "announcements": announcements}
    return render(request, 'club_app/member/member_sessions.html', context)
