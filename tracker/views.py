from django.db.models import Max, Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Habit, Record
from .forms import AddHabit, AddRecord

# Create your views here.
def index(request):
    # habit = Habit.objects.all()

    context = {


    }
    return render(request, "tracker/index.html", context=context)


def user_home(request):
    habits = Habit.objects.filter(user=request.user)

    context = {
        'habits': habits,

    }


    return render(request, "tracker/user_home.html", context=context)


def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    records = Record.objects.filter(habit=habit)

    avg_record = records.aggregate(Avg('actual'))['actual__avg']
    max_record = records.aggregate(Max('actual'))['actual__max']

    context = {
        'habit': habit,
        'records': records,
        'avg_record': avg_record,
        'max_record': max_record,
    }

    return render(request, 'tracker/habit.html', context=context)

def create_habit(request):
    if request.method == 'POST':
        form = AddHabit(request.POST)
        if form.is_valid():
            habit = Habit.objects.create(name=form.cleaned_data['name'], goal=form.cleaned_data['goal'], user=request.user)
            habit.save()
            return HttpResponseRedirect(reverse('habit-detail', args=[habit.pk]))
        
    else:
        form = AddHabit()

    context = {
        'form': form,
    }

    return render(request, 'tracker/new_habit.html', context)


def delete_habit(request, pk):
    Habit.objects.filter(user=request.user, pk=pk).delete()

    return render(request, 'tracker/habit_deleted.html')


def add_record(request, pk):
    habit = get_object_or_404(Habit, pk=pk, user=request.user)

    if request.method == 'POST':
        form = AddRecord(request.POST)
        if form.is_valid():
            record = Record.objects.create(date=form.cleaned_data['date'], actual=form.cleaned_data['actual'], habit=habit)
            record.save()
            return HttpResponseRedirect(reverse('habit-detail', args=[habit.pk]))

    else:
        form = AddRecord()

    context = {
        'form': form,
    }

    return render(request, 'tracker/new_record.html', context)
