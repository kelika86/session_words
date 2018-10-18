from django.shortcuts import render, redirect, HttpResponse
import time

def index(request):
    if not 'word' in request.session:
        request.session['word']=[]
    context={
        'word':request.session['word'],
        'time':time.strptime('%d %b %y'), 
    }
    return render(request,'first_app/index.html', context)

def process(request):
    print(request.session['word'])
    request.session['word']=request.POST['word']
    return redirect('/session_words')



def clear(request):
    request.session.clear()
    return redirect('/session_words')



# Create your views here.
