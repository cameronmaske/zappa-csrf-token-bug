from django.shortcuts import render
from .forms import Confirm


def example(request):
    form = Confirm()
    if request.method == "POST":
        form = Confirm(request.POST)
        if form.is_valid():
            return render(request, 'base.html', {"status": "worked"})

    context = {
        "form": Confirm(),
    }
    return render(request, 'base.html', context)
