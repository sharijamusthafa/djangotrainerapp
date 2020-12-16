from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
# Create your views here.
from trainer.forms import TrainerRegistrationForm,TrainerLoginForm,trainerProfileForm,applyform,filterform,skillform
from django.contrib.auth.models import User
from trainer.models import TrainerProfile
from Insadmin.models import InstituteDetails,SkillModel
def trainerRegistration(request):
    form=TrainerRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=TrainerRegistrationForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect("logg")
        else:
          context["form"]=form
          return render(request,"trainer/trainerregistration.html",context)

    return render(request,"trainer/trainerregistration.html",context)

def trainerLogin(request):
    form=TrainerLoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=TrainerLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if(user):
                login(request,user)
                return redirect("joblist")
            else:
                context["form"]=form
                return render(request,"trainer/trainerlogin.html",context)

    return render(request,"trainer/trainerlogin.html",context)

def trainerHome(request):
    return render(request,"trainer/trainerhome.html")


def createtrainerprofile(request):
    # form=trainerProfileForm(initial={"user":request.user})
    form=trainerProfileForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form =trainerProfileForm(request.POST,request.FILES)
        # form = trainerProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
            context["form"] = form
            return render(request,"trainer/trainerprofile.html",context)

    return render(request,"trainer/trainerprofile.html",context)

def listProfile(request):
    profile=TrainerProfile.objects.all()
    context={}
    context["profiles"]=profile
    return render(request,"trainer/listprofile.html",context)



def deleteProfile(request,pk):

    qs=TrainerProfile.objects.get(id=pk).delete()
    return redirect("logg")

def welcome(request):
    return render(request,"trainer/welcom.html")

def applyjob(request):
    form=applyform(initial={"name":request.user})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=applyform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("page")
        else:
            context["form"]=form
            return render(request,"trainer/apply.html",context)

    return render(request,"trainer/apply.html",context)

def pageview(request):
    return render(request,"trainer/page.html")

def listJob(request):
    job=InstituteDetails.objects.all()
    context = {}
    context["jobs"]=job
    form=filterform()
    context["form"]=form
    if request.method=="POST":
        form=filterform(request.POST)
        if form.is_valid():
            skill=form.cleaned_data.get("filter")
            job=InstituteDetails.objects.filter(skills=skill)
            context["jobs"] = job
            return render(request, "trainer/listjobb.html",context)

    return render(request, "trainer/listjobb.html",context)

def logoutView(request):
    logout(request)
    return redirect("logg")

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

    return render(request, "trainer/skill.html", context)