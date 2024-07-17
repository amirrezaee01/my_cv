from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    context = {'author':'امیرمحمد','job':'من برنامه نویسی جنگو کار میکنم','major':'دانشجوی رشته کامپیوتر'}
    return render(request,'index.html',context)
