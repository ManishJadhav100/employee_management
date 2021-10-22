from django.contrib.auth.models import Permission
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db import IntegrityError
from .models import Employee
from .forms import EmployeeForm

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
        if Employee.objects.values_list('email') == employee.email:
            return render(request, 'employeeForm.html', {'form':EmployeeForm(), 'error':'Bad data passed in. Try again.'})
        else:
            form = EmployeeForm(request.POST)
            newemployee = form.save(commit=False)
            newemployee.user = request.user
            newemployee.save()
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
