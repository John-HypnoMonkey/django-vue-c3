from django.shortcuts import render

# Create your views here.


def viewChart(request):
    context = {}
    return render(request, "chart/base.html", context)



def apiChart():
    pass
