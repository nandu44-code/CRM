from django.shortcuts import render,redirect
from .models import CustomUser,Client
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse

# Create your views here.
def user_registration(request):
    if 'useremail' in request.session:

        return redirect('home')

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
            return redirect('user-login')
        else:

            messages.error(request, 'passwords do not match')
            
    return render(request,'accounts/registration.html')


def user_login(request):

    if 'useremail' in request.session:

        return redirect('home')

    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(email=user_email)
        except CustomUser.DoesNotExist:
            user = None

        if user is not None:
            if not user.is_active:
                messages.error(request, 'Your account has been blocked')
                return redirect('user_login')
                
            user = authenticate(request, email=user_email, password=user_password)

            if user is not None:
                login(request,user)
                request.session['useremail'] = user_email
                print(user.is_special_user,'special users')
                if user.is_special_user:
                    return redirect('special-user-home')
                else:
                    return redirect('home')
            else:
                messages.error(request,'username or password is incorrect')
        else:
            messages.error(request, 'user does not exist')

    return render(request, 'accounts/login.html')

def user_logout(request):
    
    if 'useremail' in request.session:
         
        logout(request)
        
    return redirect('home')


def home(request):

    if 'useremail' not  in request.session:
        return redirect('user-login')

    count = Client.objects.all().count()
    
    return render(request, 'accounts/home.html', {'count': count})

def special_user_home(request):

    if 'useremail' not  in request.session:
        return redirect('user-login')

    return render(request, 'accounts/special_user_home.html')


def create_client(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')


        client = Client(name=name,email=email,phone=phone)
        client.save()

        return JsonResponse({'status': 'success', 'client': {
                'id':client.id,
                'name': client.name,
                'email': client.email,
                'phone': client.phone,
            }})

def update_client(request,client_id):

    try:
        client = Client.objects.get(id=client_id)

    except Client.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Client not found'})

    client.name = request.POST.get('name', client.name)
    client.email = request.POST.get('email', client.email)
    client.phone = request.POST.get('phone', client.phone)
    client.save()

    return JsonResponse({'status': 'success', 'client': {
            'id':client.id,
            'name': client.name,
            'email': client.email,
            'phone': client.phone,
        }})

def delete_client(request,client_id):
    try :
        client = Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'client not found'})
    
    client.delete()

    return JsonResponse({'status': 'success'})

def get_clients(request):
    clients = Client.objects.all().values('id', 'name', 'email', 'phone')
    return JsonResponse(list(clients), safe=False)