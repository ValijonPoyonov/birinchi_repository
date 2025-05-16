from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Countries, Employees, Dependents


def index_page(request):
     return render(request, "index.html")

def get_max_salary_employees(request, top):
     queryset = Employees.objects.all().order_by('-salary')[:top]
     return render(request,"max_salary.html",{"max_salary":queryset})

def get_dependents(request, employee_id):
     queryset=Dependents.objects.all().filter(employee=employee_id)
     employee=Employees.objects.get(employee_id=employee_id)
     contex = {'deps':queryset, 'employee':employee}
     return render(request, "dependents.html", contex)

# def list1(request):
#      countries = Employees.objects.order_by('-salary')
#      country_list = ""
#
#      for i in countries:
#           country_list = country_list + f"<li>{i.first_name} {i.salary}</li>"
#      return HttpResponse(f"<ol>{country_list}</ol>")