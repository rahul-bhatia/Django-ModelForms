from django.shortcuts import render
from .form import EnForm
# Create your views here.
def home(request):
	if request.method=="POST":
		f=EnForm(request.POST)
		if f.is_valid():
			f.save()
			fm=EnForm()
			return render(request,'home.html',{'fm':fm,'msg':'Noted'})
		else:
			return render(request,'home.html',{'fm':f,'msg':'Check Error'})
	else:
		fm=EnForm()
		return render(request,'home.html',{'fm':fm})