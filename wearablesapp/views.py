from django.http import HttpResponse
from django.shortcuts import render
from .forms import ActivityPeriodForm

# Create your views here.
def index(request):
    context = {
        "doc_title" : "Резултати от обработката и анализа на данните",
    }
    return render(request,'results.html', context)

def activity(request):
    if request.method == 'POST':
        form = ActivityPeriodForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data['start_interval'].value()
            end = form.cleaned_data['end_interval'].value()
            split = form.cleaned_data['time_split'].value()
            activity = wearableProc.r['prepare_interval_activity_data']

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
