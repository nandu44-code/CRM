from django.shortcuts import redirect

def is_special_user(view_func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('user-login')
        
        if not request.user.is_special_user:
            return redirect('error-page')

        return view_func(request,*args,**kwargs)

    return wrapper