from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import BookFormSet, BookForm
from .models import Author, Book


def create_book(request, pk):
    author = Author.objects.get(id=pk)
    books = Book.objects.filter(author=author)
    form = BookForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return HttpResponse("success")
        else:
            return render(request, "partials/book_form.html", context={
                "form": form
            })

    context = {
        "form": form,
        "author": author,
        "books": books
    }

    return render(request, "create_book.html", context)


def create_book_form(request):
    form = BookForm()
    context = {"form": form}
    return render(request, "partials/book_form.html", context)
