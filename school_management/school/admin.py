from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Student, LibraryHistory, FeesHistory

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'student_class')  # Fields to display in the admin list view
    search_fields = ('name',)  # Allow searching by name

@admin.register(LibraryHistory)  
class LibraryHistoryAdmin(admin.ModelAdmin):
    list_display = ('student', 'book_title', 'borrowed_date', 'returned_date')  # Fields to display in the admin list view
    list_filter = ('student', 'borrowed_date')  # Add filters for easy navigation
    search_fields = ('book_title', 'student__name', 'student__student_class')  # Allow searching by book title, student's name, and class

@admin.register(FeesHistory)
class FeesHistoryAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'payment_date', 'status')  # Fields to display in the admin list view
    list_filter = ('student', 'status', 'payment_date')  # Add filters for easy navigation
    search_fields = ('student__name',)  # Allow searching by student's name