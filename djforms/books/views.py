from django.shortcuts import redirect, render
from .forms import BookFormSet, BookForm
from .models import Author, Book


def create_book(request, pk):
    author = Author.objects.get(id=pk)
    books = Book.objects.filter(author=author)
    formset = BookFormSet(request.POST or None)

    if request.method == "POST":
        if formset.is_valid():
            formset.instance = author
            formset.save()
            return redirect("create-book", pk=author.id)

    context = {"formset": formset, "author": author, "books": books}

    return render(request, "create_book.html", context)


def create_book_form(request):
    form = BookForm()
    context = {"form": form}
    return render(request, "partials/book_form.html", context)
