from django.shortcuts import render
from .forms import WnForm
# Create your views here.
def home(request):
	if request.method=="POST":
		f=WnForm(request.POST)
		if f.is_valid():
			f.save()
			fm=WnForm()
			return render(request,'home.html',{'fm':fm,'msg':'Noted'})
		else:
			return render(request,'home.html',{'fm':f,'msg':'Check Error'})
	else:
		fm=WnForm()
		return render(request,'home.html',{'fm':fm})