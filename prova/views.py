from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home (request):
     return render (request, 'home.html')
# Create your views here.
def enter(request):
    if (request.method == 'POST'):
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=password)
         if user is not None:
             login(request, user)
             messages.add_message(request, messages.INFO, 'Seja bem vindo de volta!')
             return redirect ('/prova/')

         else:
             messages.add_message(request, messages.INFO, 'Usuario e senha incorretos')
             return render (request, 'login.html')


        
            
    if (request.method == 'GET'):
        return render (request, 'login.html')

           
              
           

   

