from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import LoginForm, RegistryForm
from .services import get_activities, create_user, user_access

# Create your views here.

def index(req):
    return render(req, 'home_index.html', {
        'activities':get_activities()
    })


def signup(req):
    method = req.method
    if method == 'POST':
        form = RegistryForm(req.POST)
        try:
            create_user(form)
            return redirect('/accounts/login')
        except Exception as e:
            return render(req, 'signup.html', {
                'form' : form,
                'error' : e
            })
    else:
        return render(req, 'signup.html', {
            'form': RegistryForm
        })

def login_view(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)
        try:
            user_access(req, form)
            return redirect(form.cleaned_data['next'])
        except Exception as e:
            return render(req, 'login.html', {
                'form':form,
                'error':e
            })
    else:
        form = LoginForm()
        return render(req, 'login.html', {
            'form': form
        })

def logout_view(req):
    logout(req)
    return render(req, 'home_index.html', {
        'activities':get_activities()
    })