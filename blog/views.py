from django.contrib.auth.models import Permission
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Employee

# Create your views here.


def index(request):
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees':employees})

def article(request, article_id):
    return render(request, 'index.html', {'article_id':article_id})

def employeeForm(request):
    return render(request, 'employeeForm.html')

def createEmployee(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        job = request.POST.get('job')
        salary = request.POST.get('salary')
        employee = Employee()
        employee.name = name
        employee.email = email
        employee.job = job
        employee.salary = salary
        employee.save()
        return redirect('index')
    elif request.method == "POST":
        name = request.POST.get('')
        email = request.POST.get('')
        job = request.POST.get('')
        salary = request.POST.get('')
        return redirect('employeeForm')
    return redirect('index')

def editEmployeeForm(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    return render(request, 'editEmployeeForm.html', {'employee':employee})

def editEmployee(request):
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        job = request.POST.get('job')
        salary = request.POST.get('salary')
        #get old info
        employee = Employee.objects.get(pk=id)
        employee.id = id
        employee.name = name
        employee.email = email
        employee.job = job
        employee.salary = salary
        employee.save()
        return redirect('index')
    return redirect('index')

def deleteEmployee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    employee.delete()
    return redirect('index')
