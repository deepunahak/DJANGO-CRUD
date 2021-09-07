from django.shortcuts import render, redirect
from .decorators import unauthenticated_user
from .models import *
from .forms import CreateUserForm, StudentRecordForm, Academics
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account Successfully created for ' + username)

            return redirect('/login/')

    context = {'form': form}
    return render(request, 'student_crud/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('/home/')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'student_crud/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('welcome')


@login_required(login_url='login')
def home(request):
    students = StudentInfo.objects.all()
    context = {"students": students}
    return render(request, 'student_crud/dashboard.html', context)


def student_list(request):
    context = {'students': StudentInfo.objects.all()}
    return render(request, "student_crud/welcome.html", context)


@login_required(login_url='login')
def student_form(request, roll_no=0):
    # formset = StudentRecordsForm(request.POST)
    # if request.method == 'POST':
    #     formset = StudentRecordsForm(request.POST)
    #     if formset.is_valid():
    #         formset.save()
    #
    #         return redirect('/home/')
    # print(formset)
    # context = {'form': formset}
    # return render(request, 'student_crud/student_detail.html', context)
    # if request.method == "GET":
    #     if id == 0:
    #         form = [StudentRecordForm(), Academics()]
    #     else:
    #         student = StudentInfo.objects.get(roll_no=roll_no)
    #         form = StudentRecordForm(instance=student)
    #     return render(request, "Student_crud/student_detail.html", {'form': form})
    # else:
    #     if id == 0:
    #         form = (request.POST)
    #     else:
    #         student = StudentInfo.objects.get(roll_no=roll_no)
    #         form = StudentRecordForm(request.POST, instance= student)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('/home/')

    form = [StudentRecordForm(), Academics()]
    if request.method == 'POST':

        form = [StudentRecordForm(request.POST), Academics(request.POST)]
        print(form[0].fields)
        print(form[0])
        print("************************************************")
        if form[0].is_valid() and form[1].is_valid():
            form[0].save()
            form[1].save()
    return render(request, "Student_crud/student_detail.html", {'form': form})

# @login_required(login_url='login')
# def updateStudent(request, roll_no):
#
#     student = StudentInfo.objects.get(roll_no=roll_no)
#     form = StudentInfo(instance=student)
#
#     if request.method == 'POST':
#         form = StudentInfo(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#
#             return redirect('home')
#
#     context = {'form': form}
#     return render(request, 'student_crud/student_detail.html', context)


@login_required(login_url='login')
def deleteStudent(request, roll_no):
    student = StudentInfo.objects.get(roll_no=roll_no)
    if request.method == "POST":
        student.delete()

        return redirect('home')

    context = {'item': student}
    return render(request, 'student_crud/delete.html', context)
