from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UsernameForm

from members.models import MemberData
from django.contrib.auth.models import User


def index(request):
    if request.method == 'POST':
        form = UsernameForm(request.POST)

        if form.is_valid():
            #form.cleaned_data['username']
            user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password'])
            member = MemberData()
            member.name = form.cleaned_data['username']
            user.save()
            member.save()
            return HttpResponseRedirect('/m/' + member.name)

    else:
        form = UsernameForm()

    return render(request, 'joinsite/index.html', {'form': form})
