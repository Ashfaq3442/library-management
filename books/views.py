from django.shortcuts import render, redirect,get_object_or_404
from .models import Book
from .forms import BookForm

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

# Mark a book as returned (available)
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Update the book to available and clear borrower details
    book.is_available = True
    book.borrower_name = ''
    book.borrower_contact = ''
    book.borrower_address = ''
    book.save()
    return redirect('book_list')
# Create your views here.
