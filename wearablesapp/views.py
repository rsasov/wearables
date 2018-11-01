from django.http import HttpResponse
from django.shortcuts import render
from .forms import ActivityPeriodForm

# Create your views here.
def index(request):
    return render(request,'results.html')

def activity(request):
    form = None
    if request.method == 'POST':
        form = ActivityPeriodForm(request.POST or None)
    #if form.is_valid():
        # TODO: ADD GRAPHICS

    #else:
        # TODO: CREATE FORM
    context = {
        "form": form,
    }
    return render(request,'activity.html',context)

def test(request):
    return HttpResponse("Hello there")
