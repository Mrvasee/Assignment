from django.shortcuts import render
import datetime
import random
import json 
import urllib.request 
from .models import Intern_Detail
from django.contrib import messages
def Home(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    quote = random.choice(["Quote 1", "Quote 2", "Quote 3"])
     
    return render(request, 'home.html', {'time': current_time, 'quote': quote})
def About(request):
    return render(request,'about.html')
def weather_Info(request): 
	if request.method == 'POST': 
		city = request.POST['city'] 
		source = urllib.request.urlopen( 
			'http://api.openweathermap.org/data/2.5/weather?q='
					+city+'&appid=828652866630e18880873ed9272a9a8a').read() 
		list_of_data = json.loads(source)
		data = { 
			"country_code": str(list_of_data['sys']['country']), 
			"coordinate": str(list_of_data['coord']['lon']) + ' '
						+ str(list_of_data['coord']['lat']), 
			"temp": str(list_of_data['main']['temp']) + 'k', 
			"pressure": str(list_of_data['main']['pressure']), 
			"humidity": str(list_of_data['main']['humidity']), 
		}       
	else: 
		data ={} 
	return render(request, "weather_info.html", data) 

def form_submission(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        pno=request.POST.get('pno')
        degree=request.POST.get('degree')
        field=request.POST.get('field')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zipcode=request.POST.get('zipcode')
        Intern_Detail.objects.create(Full_name=name,Email=email,Phone_No=pno,Degree=degree,Field=field,Address=address,City=city,State=state,Pincode=zipcode)
        return render(request, 'intern_form.html')
    return render(request,'intern_form.html')

def Intern_Login(request):

    return render(request,'intern_login.html')

def view_details(request):
    if request.method=="GET":
        mail=request.GET.get('email')
        try:
            details = Intern_Detail.objects.filter(Email=mail)
            return render(request,'intern_details.html',{'data':details})
        except Intern_Detail.DoesNotExist:
            messages.error(request,'Email Does Not Exists')
            return render(request,'intern_login.html')
    return render(request, 'intern_login.html')

# Create your views here.
