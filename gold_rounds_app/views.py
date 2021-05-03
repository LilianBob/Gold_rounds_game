from django.shortcuts import render, redirect
import random
from time import localtime, strftime
from datetime import date

def index(request):
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
        # context = {
        #     "activities": request.session['activities']
        # }
    return render(request, "show.html")
def find_gold(request):
    if request.method == "POST" or request.method == "GET":
        location = request.POST['location']
        gold_count = request.session['gold']
        activities = request.session['activities']
        if location == 'farm':
            thisgoldRound = random.randint(10, 20)
            gold_count += thisgoldRound
            request.session['gold'] = gold_count
        if location == 'cave':
            thisgoldRound = random.randint(5, 10)
            gold_count += thisgoldRound
            request.session['gold']= gold_count
        if location == 'house':
            thisgoldRound = random.randint(2, 5)
            gold_count += thisgoldRound
            request.session['gold']= gold_count
        if location == 'casino':
            thisgoldRound = random.randint(-50, 50)
            gold_count += thisgoldRound
            request.session['gold']= gold_count
        
        date = strftime("%b %d, %Y", localtime())
        time = strftime("%I:%M %p", localtime())

        if thisgoldRound >= 0:
            str = f"Earned {thisgoldRound} from the {location} on {date}, {time}"            
        else:
            thisgoldRound *= -1
            str = f"Lost {thisgoldRound} from the {location} on {date}, {time}"
        activities.insert(0, str)
        request.session['activities'] = activities
    return redirect('/')
def reset(request):
    if request.method == "POST":
        if 'reset' in request.POST:
            request.session.flush()
    return redirect("/")

# Create your views here.
