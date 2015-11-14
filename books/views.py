from django.shortcuts import render, render_to_response, get_object_or_404
from models import Book, Author
from django.http import HttpResponse, HttpResponseRedirect
from forms import CreateBookForm, CreateAuthorForm, ChangeBookForm, ChangeAuthorForm
# Create your views here.
def IndexShow(request):
    book_set = Book.objects.all()
    if request.method=="POST":
        if "search" in request.POST:
            search_type = request.POST.get("method")
            search_content = request.POST.get("content")
            if search_type=="author_name":
                authors = Author.objects.filter(Name=search_content)
                if authors:
                    book_set = []
                    for author in authors:
                    	book_set.extend(author.books.all())
                else:
                    book_set = {}
            elif search_type=="isbn":
                book_set = Book.objects.filter(ISBN=search_content)
            else:
                book_set = Book.objects.filter(Title=search_content)
    	elif "addauthor" in request.POST:
        	return HttpResponseRedirect("../create_author/")
    	elif 'addbook' in request.POST:
            return HttpResponseRedirect("../create_book/")
    	elif "delete" in request.POST:
            if Book.objects.all():
                ISBN = request.POST["delete"]
                book = Book.objects.get(ISBN=ISBN)
                if book:
                    book.delete()
                    book_set = Book.objects.all()
    	else:
	   		book_set = Book.objects.all()
    authors = []
    for author in Author.objects.all():
        authors.append({"author":author,"booklist":author.books.all()})
    return render(request, 'index.html', {'books':book_set, 'authors':authors})
def CreateBook(request):
    if request.method == 'POST':
        if "addauthor" in request.POST:
            return HttpResponseRedirect("../create_author/")
        else:
            form = CreateBookForm(request.POST)
            if form.is_valid():
                book = form.save()
                return HttpResponseRedirect("../books/"+str(book.ISBN))
    else:
        form = CreateBookForm()
    return render(request, "create_book.html",{"form":form})
def ChangeBook(request,ISBN):
    book =  get_object_or_404(Book,ISBN=ISBN)
    data = {"ISBN":book.ISBN, "Title":book.Title, "AuthorID":book.AuthorID, "Publisher":book.Publisher, "PublishDate":book.PublishDate}
    if request.method == 'POST':
        form = ChangeBookForm(request.POST, initial=data)
        if form.is_valid():
            if form.has_changed():
                book.ISBN = form.cleaned_data['ISBN']
                book.Title = form.cleaned_data['Title']
                book.AuthorID = form.cleaned_data['AuthorID']
                book.Publisher = form.cleaned_data['Publisher']
                book.PublishDate = form.cleaned_data['PublishDate']
                book.Price = form.cleaned_data["Price"]
                book.save()
            return HttpResponseRedirect("../../"+ISBN)
    else:
        form = ChangeBookForm(initial=data)
    return render(request, 'change_book.html', {'form':form,'Title':book.Title})

def ShowBook(request,ISBN):
    book = get_object_or_404(Book,ISBN=ISBN)
    return render(request,"show_book.html",{'book':book, 'author':book.AuthorID,"booklist":book.AuthorID.books.all()})
def CreateAuthor(request):
    if request.method == 'POST':
        form = CreateAuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return HttpResponseRedirect("../authors/"+str(author.AuthorID))
    else:
        form = CreateAuthorForm()
    return render(request, "create_author.html",{"form":form})

def ChangeAuthor(request,AuthorID):
    author = get_object_or_404(Author, AuthorID=AuthorID)
    data = {"AuthorID":author.AuthorID, "Name":author.Name, "Age":author.Age,
            "Country":author.Country,}
    if request.method == 'POST':
        form = ChangeAuthorForm(request.POST,initial=data)
        if form.is_valid():
            if form.has_changed():
                author.AuthorID = form.cleaned_data["AuthorID"]
                author.Name = form.cleaned_data["Name"]
                author.Age = form.cleaned_data["Age"]
                author.Country = form.cleaned_data["Country"]
                author.save()
            return HttpResponseRedirect("../../"+AuthorID)
    else:
        form = ChangeAuthorForm(initial=data)
    return render(request, 'change_author.html', {'form':form, 'Name':author.Name})

def ShowAuthor(request,AuthorID):
	author = get_object_or_404(Author,AuthorID=AuthorID)
	return render(request,"show_author.html",{'author':author,"booklist":author.books.all()})
