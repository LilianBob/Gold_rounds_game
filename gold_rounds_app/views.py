from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')
def find_gold(request):
    if request.method=="POST":
        if 'red' in request.session:
            request.method['name']= name
            request.mthod['gold_count_goal']= goal
            request.method['team']= 'red'
    return render(request, "show.html")
def reset(request):
    request.session.flush()
    return redirect('/')

# Create your views here.
