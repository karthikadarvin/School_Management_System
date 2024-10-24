from django.urls import path
from .views import (index ,register, user_login, home,student_list,
                    add_student, edit_student, delete_student,library_history_list,
                    fetch_student_data,add_library_history, edit_library_history,
                    delete_library_history, fetch_library_history,fees_history_list,
                    add_fees_history, edit_fees_history, delete_fees_history)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),  
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/',home ,name='home'),
    path('student/', student_list, name='student_list'),
    path('add/', add_student, name='add_student'),
    path('edit/<int:student_id>/', edit_student, name='edit_student'),
    path('delete/<int:student_id>/', delete_student, name='delete_student'),
    path('fetch/', fetch_student_data, name='fetch_student_data'),
    path('library/history/', library_history_list, name='library_history_list'),
    path('library/add/', add_library_history, name='add_library_history'),
    path('library/edit/<int:history_id>/', edit_library_history, name='edit_library_history'),
    path('library/delete/<int:history_id>/', delete_library_history, name='delete_library_history'),
    path('library/history/<int:student_id>/', fetch_library_history, name='fetch_library_history'),
    path('fees/', fees_history_list, name='fees_history_list'),
    path('fees/add/', add_fees_history, name='add_fees_history'),
    path('fees/edit/<int:pk>/', edit_fees_history, name='edit_fees_history'),
    path('fees/delete/<int:pk>/', delete_fees_history, name='delete_fees_history'),

]
