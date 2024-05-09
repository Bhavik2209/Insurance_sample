from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
import joblib
model = joblib.load('static/model_regressor')

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def prediction(request):
    if request.method=="POST":
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('gender'))
        bmi = int(request.POST.get('bmi'))
        children = int(request.POST.get('child'))
        smoker = int(request.POST.get('smoker'))
        region = int(request.POST.get('region'))
        
        
        pred = round(model.predict([[age,sex,bmi,children,smoker,region]])[0])
        output = {
            "output":pred
        }

        return render(request,"prediction.html",output)


    else:
        return render(request,"prediction.html")
    
# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
        
#         # Send email
#         send_mail(
#             'New message from your website',
#             f'Name: {name}\nEmail: {email}\nMessage: {message}',
#             email, 
#             ['bhavikrohit22@gmail.com'],
#             fail_silently=False,
#         )
    
#         return render(request, 'contact.html')
#     return render(request, 'contact.html')
