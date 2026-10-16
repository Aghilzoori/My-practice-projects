from .models import Candidates
from counter.models import Vote
from django.db.models import Count
from .forms import CandidatesForms
from django.contrib import messages
from .resources import VoteResource
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

def main(request):
    context = {'candidates':Candidates.objects.all(), 
               'results_vote': (Vote.objects.values("candidate_id", "candidate_id__fullname").annotate(vote_count=Count("id")).order_by("-vote_count")),
               'participants': Vote.objects.all()
               }
    
    return render(request, "main.html", context)

def creat_candidate(request):
    context = {}

    if request.method == "POST":

        form = CandidatesForms(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "کاندید مورد نظر اضافه شد")

            return redirect('main')
        
        else:

            context["form"] = form
    else:

        form = CandidatesForms()

        context["form"] = form

    return render(request, "c.html", context)

def edit_candidate(request, pk):    
    profile = Candidates.objects.get(id=pk)

    form = CandidatesForms(instance=profile)

    if request.method == 'POST':

        form = CandidatesForms(request.POST, instance=profile)

        if form.is_valid():

            form.save()

            messages.success(request, "ویرایش با موفقیت انجام شد")

            return redirect('main')

    context = {'form': form}

    return render(request, 'c.html', context)

def delete_candidate(request, pk):
    chat = get_object_or_404(Candidates, id=pk)

    chat.delete()

    messages.success(request, "کاندید مورد نظر حذف شد")

    return redirect("main")
    
def export_excel(request):
    dataset = VoteResource().export()
    response = HttpResponse(
        dataset.xlsx,
        content_type=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        ),
    )
    response["Content-Disposition"] = 'attachment; filename="data.xlsx"'
    return response

# Create your views here.
