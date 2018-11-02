from django.http import HttpResponse
from django.shortcuts import render
from .forms import ActivityPeriodForm
from rpy2.robjects.packages import importr
from rpy2.robjects import r


def prepare_plotting_data(start,end,interval):
    r.load("~/Documents/django-rsas/wearables/.RData")
    wearableProc = importr("wearableProc", lib_loc="~/Documents/django-rsas/wearables/R/x86_64-pc-linux-gnu-library/3.4")
    utils = importr('utils')
    ggplot = importr('ggplot2')
    stringr = importr("stringr", lib_loc="~/Documents/django-rsas/wearables/R/x86_64-pc-linux-gnu-library/3.4")

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
        start = form['start_interval'].value()
        end = form['end_interval'].value()
        interval = form['time_split'].value()
        prepare_plotting_data('start','end','interval')

            #start_interval = form.cleaned_data['start_interval']
            #end_interval = form.cleaned_data['end_interval']
            #time_split = form.cleaned_data['time_split']
            #context = {
            #    "doc_title" : "Активност за въведен период",
            #}

        return render(request,'activity.html')
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
