from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib import messages
# Create your views here.
def user_registration(request):


    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('usertype')
        print("..............")
        print(password)
        print(confirm_password)
        if user_type == 'special_user':
            special_user = True
        else:
            special_user = False
        print(CustomUser.objects.all(),'all customers')
        username_checking = CustomUser.objects.filter(username = username)
        email_checking = CustomUser.objects.filter(email = email)
        if username_checking.exists():
            messages.error(request,"username is already taken") 
            return redirect('user-registration')
        elif  email_checking.exists():
            messages.error(request, "email is already taken")
            return redirect('user-registration')
        elif password == confirm_password:
            print("J")
            my_user = CustomUser.objects.create_user(email = email, username = username, password = password, is_special_user = special_user)
            my_user.save()
            print(my_user)
        else:

            messages.error(request, 'passwords do not match')
            
    return render(request,'accounts/registration.html')