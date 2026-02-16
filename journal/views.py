from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import JournalEntryForm
from .gemini_utils import analyze_mood
from .models import JournalEntry


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('journal_home')
    else:
        form = UserCreationForm()
    return render(request, 'journal/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('journal_home')
    else:
        form = AuthenticationForm()
    return render(request, 'journal/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('journal_home')

@login_required
def journal_home(request):
    entries = JournalEntry.objects.filter(user=request.user)
    return render(request, 'journal/home.html', {'entries': entries})

@login_required
def add_entry(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.mood = analyze_mood(entry.content)
            entry.save()
            return redirect('journal_home')
    else:
        form = JournalEntryForm()
    return render(request, 'journal/add_entry.html', {'form': form})

@login_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(JournalEntry, id=entry_id, user=request.user)

    if request.method == 'POST':
        form = JournalEntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.mood = analyze_mood(entry.content)
            entry.save()
            return redirect('journal_home')
    else:
        form = JournalEntryForm(instance=entry)

    return render(request, 'journal/edit_entry.html', {'form': form, 'entry': entry})

@require_POST
@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(JournalEntry, id=entry_id, user=request.user)
    entry.delete()
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({"success": True})
    return redirect("home")