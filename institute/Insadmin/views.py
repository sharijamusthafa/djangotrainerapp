from django.shortcuts import render,redirect

# Create your views here.
from Insadmin.models import InstituteDetails,SkillModel,filterskill
from Insadmin.forms import InstituteForm,skillform,filterform

def jobView(request):
    form=InstituteForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=InstituteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listjob")
        else:
            context["form"]=form
            return render(request, "inst/jobdetails.html", context)

    return render(request,"inst/jobdetails.html",context)

def listJob(request):
    job = InstituteDetails.objects.all()
    context = {}
    context["jobs"] = job
    form=filterform()
    context["form"]=form
    if request.method=="POST":
        form=filterform(request.POST)
        if form.is_valid():
            skill=form.cleaned_data.get("filter")
            job=InstituteDetails.objects.filter(skills=skill)
            context["jobs"] = job
            return render(request, "inst/listjob.html", context)
    return render(request, "inst/listjob.html", context)



def skillview(request):
    form=skillform()
    context={}
    skill= SkillModel.objects.all()
    context["form"]=form
    context["skill"]=skill
    if request.method=="POST":
        form=skillform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("skill")

    return render(request, "inst/skill.html", context)

