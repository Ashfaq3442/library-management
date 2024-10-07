from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'is_available', 'borrower_name', 'borrower_contact', 'borrower_address']

