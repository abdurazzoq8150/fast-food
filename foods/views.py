from django.shortcuts import render, redirect
from .forms import *
from django.views import View

# Create your views here.

class UserRegistration(View):
    def get(self, request):
         form = UserRegistrationForm
         context = {'form': form}
         request.title = "User registration"
         return render(request, 'foods/registration.html', context) 
         
         
    def post(self,request):
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            # formdata = form.cleaned_data
            # del formdata['password2']

            # User = User(**formdata)
            # User.set_password(formdata['password1'])
            # User.save()
            return redirect("registration")
        context = {'form': form}
        return render(request, 'foods/registration.html', context)

        
