from django import forms
from .models import CustomUser,Student,LibraryHistory,FeesHistory

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'role']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'student_class'] 


class LibraryHistoryForm(forms.ModelForm):
    class Meta:
        model = LibraryHistory
        fields = ['student', 'book_title', 'borrowed_date', 'returned_date']  


class FeesHistoryForm(forms.ModelForm):
    class Meta:
        model = FeesHistory
        fields = ['student', 'amount', 'payment_date', 'status']