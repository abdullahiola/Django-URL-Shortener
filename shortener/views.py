from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Url
import uuid
# Create your views here

def home(request):
  return render(request,'index.html')

def create(request):
  if request.method =="POST":
    link = request.POST['link']
    uid= str(uuid.uuid4())[:5]
    new_url= Url(url=link,uuid=uid)
    new_url.save()
    return HttpResponse(uid)
  
def goto(request,pk):
  url_details = Url.objects.get(uuid=pk)
  return redirect('https://'+url_details.url)

