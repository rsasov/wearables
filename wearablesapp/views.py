from django.http import HttpResponse
from django.shortcuts import render
from .forms import ActivityPeriodForm
from rpy2.robjects.packages import importr
from rpy2.robjects import r

# Create your views here.
def index(request):
    context = {
        "doc_title" : "Резултати от обработката и анализа на данните",
    }
    return render(request,'results.html', context)

def activity(request):
    r.load("~/Documents/django-rsas/wearables/.RData")
    wearableProc = importr("wearableProc", lib_loc="~/Documents/django-rsas/wearables/R/x86_64-pc-linux-gnu-library/3.4")
    if request.method == 'POST':
        form = ActivityPeriodForm(request.POST)
        #if form.is_valid():
            #start_interval = form.cleaned_data['start_interval']
            #end_interval = form.cleaned_data['end_interval']
            #time_split = form.cleaned_data['time_split']
            #context = {
            #    "doc_title" : "Активност за въведен период",
            #}

        return render(request,'activity.html',context)
    else:
        form = ActivityPeriodForm()
        context = {
            "doc_title" : "Проверка на активност",
            "form" : form,
        }
        return render(request,'activity_form.html',context)

    def post(self,request):
        form = ActivityPeriodForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data
