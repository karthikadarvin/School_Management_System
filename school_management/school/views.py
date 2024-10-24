from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm , StudentForm, LibraryHistoryForm, FeesHistoryForm
from .models import CustomUser,Student ,LibraryHistory,FeesHistory
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the index page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'home1.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form, 'student': student})


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'delete_student.html', {'student': student})


def fetch_student_data(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def library_history_list(request):
    history_records = LibraryHistory.objects.all()  
    return render(request, 'library_history_list.html', {'history_records': history_records})


def add_library_history(request):
    if request.method == "POST":
        form = LibraryHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library_history_list')
    else:
        form = LibraryHistoryForm()
    
    # Fetch students to populate the dropdown
    students = Student.objects.all()
    
    return render(request, 'add_library_history.html', {'form': form, 'students': students})



def edit_library_history(request, history_id):
    history_record = get_object_or_404(LibraryHistory, id=history_id)
    if request.method == "POST":
        form = LibraryHistoryForm(request.POST, instance=history_record)
        if form.is_valid():
            form.save()
            return redirect('library_history_list')
    else:
        form = LibraryHistoryForm(instance=history_record)
    return render(request, 'edit_library_history.html', {'form': form})


def delete_library_history(request, history_id):
    history_record = get_object_or_404(LibraryHistory, id=history_id)
    if request.method == "POST":
        history_record.delete()
        return redirect('library_history_list')
    return render(request, 'delete_library_history.html', {'history': history_record})


def fetch_library_history(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    history_records = LibraryHistory.objects.filter(student=student)
    return render(request, 'library_history_list.html', {'student': student, 'history_records': history_records})


def fees_history_list(request):
    fees_history = FeesHistory.objects.all()
    return render(request, 'fees_history_list.html', {'fees_history': fees_history})

def add_fees_history(request):
    if request.method == 'POST':
        form = FeesHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fees_history_list')  # Adjust the URL as needed
    else:
        form = FeesHistoryForm()
    
    students = Student.objects.all()
    return render(request, 'fees_history_form.html', {'form': form, 'students': students, 'title': 'Add Fees History'})

def edit_fees_history(request, pk):
    fees_history = get_object_or_404(FeesHistory, pk=pk)
    if request.method == 'POST':
        form = FeesHistoryForm(request.POST, instance=fees_history)
        if form.is_valid():
            form.save()
            return redirect('fees_history_list')  # Adjust the URL as needed
    else:
        form = FeesHistoryForm(instance=fees_history)

    students = Student.objects.all()
    return render(request, 'fees_history_form.html', {'form': form, 'students': students, 'title': 'Edit Fees History'})


def delete_fees_history(request, pk):
    fees_history = get_object_or_404(FeesHistory, pk=pk)
    if request.method == 'POST':
        fees_history.delete()
        return redirect('fees_history_list')
    return render(request, 'delete_fees.html', {'fees_history': fees_history})
