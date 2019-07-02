from django.shortcuts import render
from .models import Habit, Record
# Create your views here.



# View all your habits- / or /habits/

def index(request):

    habit = Habit.objects.all()
    
    context = { 'habit': habit,
            
    }
    return render(request, 'index.html' , context=context)


# create a habit - /habits/new/ - Get & post

def create_habit(request)


    context = { 
            
    }

    return render(request, 'create_habit.html' , context=context)


# view habit records- / habits /<pk>
def view_record(request)

context = { 
            
    }

    return render(request, 'view_record.html' , context=context)



# add record - habits/ <pk>/ new-record/

# edit record - 



 