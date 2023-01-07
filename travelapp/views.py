from django.shortcuts import HttpResponse, render
from . models import Place,Team_members

# Create your views here.
def index(request):
   data = Place.objects.all()
   team_members = Team_members.objects.all()
   return render(request,'index.html',{'destination': data,'team_members': team_members})
