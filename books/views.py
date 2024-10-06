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



# Borrow a book and mark it as unavailable
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == "POST":
        borrower_name = request.POST.get('borrower_name')
        borrower_contact = request.POST.get('borrower_contact')
        borrower_address = request.POST.get('borrower_address')
        
        # Update the book status to unavailable and save the borrower details
        book.is_available = False
        book.borrower_name = borrower_name
        book.borrower_contact = borrower_contact
        book.borrower_address = borrower_address
        book.save()
        
        return redirect('book_list')

    return render(request, 'books/borrow_book.html', {'book': book})