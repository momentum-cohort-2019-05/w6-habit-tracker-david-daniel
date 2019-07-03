from datetime import timedelta
from django.db.models import Max, Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Habit, Record, Observer
from .forms import AddHabit, AddRecord, AddObserver, this

# Create your views here.
def index(request):
    # habit = Habit.objects.all()

    context = {


    }
    return render(request, "tracker/index.html", context=context)


def user_home(request):
    habits = Habit.objects.filter(user=request.user)

    observing = Observer.objects.filter(user=request.user)


    context = {
        'habits': habits,
        'observing': observing,

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
            if Record.objects.filter(habit=habit):
                delta = timedelta(days=1)
                last_record_date = Record.objects.filter(habit=habit).latest('date').date
                record_date = form.cleaned_data['date']
                if record_date != (last_record_date + delta):
                    last_record_date += delta
                    while last_record_date < record_date:
                        blank_record = Record.objects.create(date=last_record_date, habit=habit)
                        blank_record.save()
                        last_record_date += delta
            record = Record.objects.create(date=form.cleaned_data['date'], actual=form.cleaned_data['actual'], habit=habit)
            record.save()
            return HttpResponseRedirect(reverse('habit-detail', args=[habit.pk]))

    else:
        form = AddRecord()

    context = {
        'form': form,
    }

    return render(request, 'tracker/new_record.html', context)


def add_observer(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request.method == 'POST':
        form = AddObserver(request.POST)
        if form.is_valid():
            new_observer = Observer.objects.create(habit=habit, user=form.cleaned_data['username'])
            new_observer.save()
            return HttpResponseRedirect(reverse('habit-detail', args=[habit.pk]))

    else:
        form = AddObserver()

    context = {
        'form': form, 
    }

    return render(request, 'tracker/new_observer.html', context)


def edit_record(request, pk):
    if request.method == 'POST':
        form = this(request.POST)
        if form.is_valid():
            record = Record.objects.get(pk=pk)
            record.actual = form.cleaned_data["actual"]
            record.save()
            return HttpResponseRedirect(reverse('habit-detail', args=[record.habit.pk]))
    else:

        form = this()

    return render(request, 'tracker/edit_record.html' , {'form': form})
