from django.shortcuts import render

# Create your views here.


def hello(request):
    return render(request, 'hello.html')

# 변화는_우리로_인하여
