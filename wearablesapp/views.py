from django.http import HttpResponse
from django.shortcuts import render
from .forms import ActivityPeriodForm
from rpy2.robjects.packages import importr
from rpy2.robjects import r

def prepare_plotting_data(start,end,interval):
    r.load("~/Documents/django-rsas/wearables/.RData")
    wearableProc = importr("wearableProc", lib_loc="~/Documents/django-rsas/wearables/R/x86_64-pc-linux-gnu-library/3.4")
    wearableProc.prepare_interval_activity_data(start,end,interval)

# Create your views here.
def index(request):
    context = {
        "doc_title" : "Резултати от обработката и анализа на данните",
    }
    return render(request,'results.html', context)

def activity(request):
    if request.method == 'POST':
        form = ActivityPeriodForm(request.POST)
        start = request.POST['start_time']
        end = request.POST['end_time']
        interval = request.POST['time_split']
        prepare_plotting_data(start,end,interval)
        return render(request,'activity.html', {"doc_title" : "Активност за въведения интервал"})
    else:
        form = ActivityPeriodForm()
        context = {
            "doc_title" : "Проверка на активност",
            "form" : form,
        }
        return render(request,'activity_form.html',context)
