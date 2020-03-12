from django.shortcuts import render, redirect
from .models import Author, Book

# Book functions
def books(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, "index.html", context)

def add_book(request):
    if request.POST['title'] and request.POST['desc']:
        Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect("/")

def view_book(request,book_id):
    thisBook = Book.objects.get(id=book_id)
    associated_authors = thisBook.authors.all()
    non_associated_authors = Author.objects.exclude(books=thisBook)
    context = {
        "thisBook": thisBook,
        "associated_authors": associated_authors,
        "non_associated_authors": non_associated_authors
    }
    return render(request, "book_info.html", context)

def add_auth_to_book(request,book_id):
    if request.POST['auth_id']:
        thisBook = Book.objects.get(id=book_id)
        thisAuthor = Author.objects.get(id=request.POST['auth_id'])
        thisBook.authors.add(thisAuthor)
    return redirect("/books/"+book_id)

# authors functions
def authors(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, "authors.html", context)

def add_author(request):
    if request.POST['fname'] and request.POST['lname'] and request.POST['notes']:
        Author.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], notes=request.POST['notes'])
    return redirect("/authors/")

def view_author(request,author_id):
    thisAuthor = Author.objects.get(id=author_id)
    associated_books = thisAuthor.books.all()
    non_associated_books = Book.objects.exclude(authors=thisAuthor)
    context = {
        "thisAuthor": thisAuthor,
        "associated_books": associated_books,
        "non_associated_books": non_associated_books
    }
    return render(request, "authors_info.html", context)

def add_book_to_auth(request,author_id):
    if request.POST['book_id']:
        thisAuthor = Author.objects.get(id=author_id)
        thisBook = Book.objects.get(id=request.POST['book_id'])
        thisAuthor.books.add(thisBook)
    return redirect("/authors/"+author_id)
    