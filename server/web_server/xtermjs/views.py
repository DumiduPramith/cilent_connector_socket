from django.shortcuts import render

# Create your views here.

def device_list(request):
    return render(request,"index.html")

def xtermjs(request,user_id):
    content = {
        "user_id" : user_id
    }
    return render(request,'xtermjs.html',context=content)