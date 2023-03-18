from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import BookData

# Create your views here.

def home(request):
    book = BookData.objects.all()
    book_name = request.GET.get('book_name')
    if book_name != '' and book_name is not None:
        book = book.filter(Name__icontains=book_name)
    paginator = Paginator(book, 6)
    page = request.GET.get('page')
    book = paginator.get_page(page)
    return render(request, 'home/index.html', {'book': book})
