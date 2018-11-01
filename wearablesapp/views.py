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
    form = None
    if request.method == 'POST':
        form = ActivityPeriodForm(request.POST or None)
    #if form.is_valid():
        # TODO: ADD GRAPHICS

    else:
        form = ActivityPeriodForm()
    context = {
        "doc_title" : "Проверка на активност",
        "form":form
    }
    return render(request,'activity.html',context)
