import requests, json
from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib.auth.decorators import  login_required
#from django.http import Http404

# Create your views here.
def home(request):
    if request.method=="POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        r = requests.get('http://api.icndb.com/jokes/random?firstName='+ first_name +'&amp;lastName='+ last_name)
        json_data = json.loads(r.text)
        data = json_data.get('value').get('joke')
        return render(request,'blog/home.html',{'data':data})
    else:
        return render(request,'blog/home.html')

@login_required()
def portfolio(request):
    return render(request,'blog/portfolio.html')

def thankyou(request):
    return render(request,'blog/thankyou.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankyou')
    else:
        form = ContactForm()
    return render(request,'blog/contact.html', {'form':form})


def page_not_found(request,exception):
    return render(request, 'blog/404.html')

# def handler500(request):
#     return render(request, '500.html', status=500)
