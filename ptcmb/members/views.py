from django.http import HttpResponse
from django.shortcuts import render

from .models import MemberData

def index(request):
    return HttpResponse("Member Hub")

def memberpage(request, name):
    member_object = MemberData.objects.get(name = name)
    context = {'Object': member_object}
    return render(request, 'members/memberpages/index.html', context)

def settingspage(request,name):
    member_object = MemberData.objects.get(name = name)
    context = {'Object': member_object}
    return render(request, 'members/settingspage/index.html', context)
