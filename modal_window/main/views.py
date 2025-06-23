from django.shortcuts import render, redirect
from .forms import FeedbackForm


def index(request):
    if request.method == 'POST':
        form_p = FeedbackForm(request.POST)
        if form_p.is_valid():
            #save form
            form_p.save()
            
    form = FeedbackForm()
    context = {
        'form': form
    }
    return render(request, 'main/index.html', context)