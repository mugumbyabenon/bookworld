from django.http import HttpResponse
from django.shortcuts import redirect,render


def unauthenticated_user(view_func):
    def wrapper_func(request, *args,**kwargs):
        if request.user.is_student or request.user.is_anonymous:
           return render(request,'../templates/disallowed.html')
           #return redirect('/')
        else:
           return view_func(request, *args, **kwargs)
    return wrapper_func
def authenticated_user(view_func):
    def wrapper_func(request, *args,**kwargs):
        if request.user.is_staff or request.user.is_anonymous:
           return render(request,'../templates/disallowed.html')
           #return redirect('/')
        else:
           return view_func(request, *args, **kwargs)
    return wrapper_func
def set(view_func):
    def wrapper_func(request, *args,**kwargs):
        if request.user.is_anonymous:
            #return view_func(request, *args, **kwargs)
           return render(request,'../templates/disallowed.html')
           #return redirect('/')
        else:
           #return redirect('/')
           return view_func(request, *args, **kwargs)
    return wrapper_func
