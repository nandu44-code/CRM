from django.shortcuts import render
from .models import CustomUser
# Create your views here.
def user_registration(request):


    if request.method == 'post':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        username_checking = CustomUser.objects.get(username = username)
        email_checking = CustomUser.objects.get(email = email)
        if username_checking.exists():
            messages.error(request,"username is already taken") 
            return redirect('user-registration')
        elif  email_checking.exists():
            messages.error(request, "email is already taken")
            return redirect('user-registration')
        # elif password == confirm_password:
            
    return render(request,'accounts/registration.html')