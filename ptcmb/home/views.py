from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext

from .forms import LoginForm

from members.models import MemberData
from django.contrib.auth.models import User

def index(request):
    form = LoginForm()
    context = {'form': form}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/join/')
    else:
        return render(request, 'home/index.html', context)

# Create your views here.
