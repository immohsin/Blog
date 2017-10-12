from django.shortcuts import render

def index(request):
    return render(request,'personal/home.html')


def contact(request):
    return render(request,'personal/basic.html',{'content':['if you would like to contact me, please click the below link','<a href="mailto:mohsinmumtaz21@gmail.com?Subject=Hi%20mohsin" target="_top">Say Hi</a>']})
