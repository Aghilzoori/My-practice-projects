from .forms import VoteForms
from django.contrib import messages
from manager.models import Candidates
from django.shortcuts import render, redirect

def home(request):
    return render(request, "home.html")

def vote_user(request):
    context = {
        "candidates": Candidates.objects.all().order_by("-id")
    }

    if request.method == "POST":

        form = VoteForms(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "رای مورد نظر ثبت شد")

            return redirect("vote_user")
    else:

        form = VoteForms()

    context["form"] = form

    return render(request, "counter_user.html", context)




# Create your views here.
