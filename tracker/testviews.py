from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import edit_record

def edit_record(request, pk):
    if request.method == 'POST':
        form = edit_record(request.POST)
        if form.is_valid():
            record = Record.objects.get()
            return HttpResponseRedirect('/thanks/')
    else:
  
        form = edit_record()

    return render(request, '', {'form': form})