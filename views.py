from django.shortcuts import render,redirect


def index(request):
    #  return redirect('pay')
 
        
    return render(request,'index.html')


def pay(request):
    return redirect('pay')



# Create your views here.
