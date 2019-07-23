from django.shortcuts import render

# Create your views here.
def home(request):
	context={
	"msg": "Hello, World!"

	}
	return render(request,"hello.html",context)
