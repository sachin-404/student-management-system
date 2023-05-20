from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Students
from .forms import StudentForm

# Create your views here.
@login_required(login_url='login')
def index(request):
    students = Students.objects.all()
    return render(request, 'students/index.html', {"students": students})

def view_student(request, id):
    student = Students.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']

            new_student = Students(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_field_of_study,
                gpa = new_gpa     
            )
            new_student.save()
            return render(request, 'students/add.html', {'form': StudentForm(), 'success': True})
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {'form': StudentForm()})

def edit(request, id):
    if request.method == 'POST':
        student = Students.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
            })
    else:
        student = Students.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})
        
def delete(request, id):
    if request.method == 'POST':
        student = Students.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.success(request, "Username or Password is incorrect!!")
    return render(request, 'students/login.html')

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
