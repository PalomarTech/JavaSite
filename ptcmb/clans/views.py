from django.http import HttpResponse
from django.shortcuts import render

from .models import Clan_Meta_Data

def index(request):
        return render(request, 'clans/clanhub/index.html')

def clanpage(request, name):
    clan_object = Clan_Meta_Data.objects.get(name = name)
    context = {'Object': clan_object, 'membercount': clan_object.member_count()}
    return render(request, 'clans/clanpage/index.html', context)
# Create your views here.
