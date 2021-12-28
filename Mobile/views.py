from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import MobileForm
from .models import MobileInformation


def form(request):
    return render(request, "Mobile/form.html")


def mobilelist(request):
    if request.method == "POST":
        fm = MobileForm(request.POST)
        if fm.is_valid():
            Brand_Name = request.POST["Brand_Name"]
            Model = request.POST["Model"]
            Color = request.POST["Color"]
            JAN_Code = request.POST["JAN_Code"]
            Image = request.POST["Image"]
            data = MobileInformation()
            data.Brand_Name = Brand_Name
            data.Model = Model
            data.Color = Color
            data.JAN_Code = JAN_Code
            data.Image = Image
            data.save()
            return render(request, "Mobile/dataTable.html", {
                "data": MobileInformation.objects.all()
            })
        else:
            return render(request, "Mobile/form.html", {'form': fm})


def autocomplete(request):
    if 'term' in request.GET:
        qs = MobileInformation.objects.filter(Model__istartswith=request.GET.get('term'))
        model = list()
        if len(qs) == 0:
            qs = MobileInformation.objects.filter(JAN_Code__istartswith=request.GET.get('term'))
            for mobile in qs:
                model.append(mobile.JAN_Code)
            return JsonResponse(model, safe=False)
        for mobile in qs:
            model.append(mobile.Model)
        return JsonResponse(model, safe=False)
    return render(request, "Mobile/dataTable.html", {
        "data": MobileInformation.objects.all()
    })


def search(request):
    if request.method == "POST":
        if request.POST["Model"] is not '':
            data = MobileInformation.objects.filter(Model=request.POST["Model"])
            return render(request, "Mobile/dataTable.html", {
                "data": data
            })
    return render(request, "Mobile/dataTable.html", {
        "data": MobileInformation.objects.all()
    })


def search_janCode(request):
    if request.method == "POST":
        if request.POST["JAN_Code"] is not '':
            print("12345")
            data = MobileInformation.objects.filter(JAN_Code=request.POST["JAN_Code"])
            return render(request, "Mobile/dataTable.html", {
                "data": data
            })
    return render(request, "Mobile/dataTable.html", {
        "data": MobileInformation.objects.all()
    })


def remove(request, JAN_Code):

    MobileInformation.objects.filter(JAN_Code=JAN_Code).delete()

    return render(request, "Mobile/dataTable.html", {
        "data": MobileInformation.objects.all()
    })


def home(request):
    return render(request, "Mobile/dataTable.html", {
        "data": MobileInformation.objects.all()
    })
