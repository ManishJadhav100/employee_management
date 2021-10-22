from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>', views.article, name='article'),
    path('employeeForm', views.employeeForm, name='employeeForm'),
    path('createEmployee', views.createEmployee, name='createEmployee'),
    path('editEmployeeForm/<int:employee_id>', views.editEmployeeForm, name='editEmployeeForm'),
    path('editEmployee', views.editEmployee, name='editEmployee'),
    path('deleteEmployee/<int:employee_id>', views.deleteEmployee, name='deleteEmployee'),
]