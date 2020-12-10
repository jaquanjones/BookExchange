from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse

from .filters import BookFilter

from .models import MainMenu
from .models import Review

from .forms import ReviewForm
from .forms import BookForm
from django.http import HttpResponseRedirect

from .models import Book

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def index(request):
    # return HttpResponse("<h1 align='center'>Hello World</h1>")
    # return render(request, 'base.html')
    # return render(request, 'bookMng/displaybooks.html')
    return render(request,
                  'bookMng/home.html',
                  {
                      'item_list': MainMenu.objects.all()
                  }
                  )


@login_required(login_url=reverse_lazy('login'))
def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'bookMng/postbook.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted
                  })



from django.shortcuts import render
from django.http import HttpResponse

from .models import MainMenu

from .forms import BookForm
from django.http import HttpResponseRedirect

from .models import Book

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .filters import BookFilter

# Create your views here.
def index(request):
    # return HttpResponse("<h1 align='center'>Hello World</h1>")
    # return render(request, 'base.html')
    # return render(request, 'bookMng/displaybooks.html')
    return render(request,
                  'bookMng/home.html',
                  {
                      'item_list': MainMenu.objects.all()
                  }
                  )


@login_required(login_url=reverse_lazy('login'))
def leave_review(request, book_id):
    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[14:]
    submitted = False
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # form.save()
            review = form.save(commit=False)
            try:
                review.username = request.user
                review.book = Book.objects.get(id=book_id)
            except Exception:
                pass
            review.save()
            return HttpResponseRedirect('/displaybooks')
    else:
        form = ReviewForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'bookMng/leave_review.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,
                      'book': book,
                  })


@login_required(login_url=reverse_lazy('login'))
def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'bookMng/postbook.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted
                  })


@login_required(login_url=reverse_lazy('login'))
def displaybooks(request):
    books = Book.objects.all()

    #data gets rendered and filters it down if there are any filters applied
    myFilter = BookFilter(request.GET, queryset=books)
    #rebuilds the result from the filter
    books = myFilter.qs

    # pagination for display books, change number of second parameter to get a customized number of books per page
    paginator = Paginator(books, 5)

    # will grab the current page from the url
    page = request.GET.get('page')

    books = paginator.get_page(page)

    for b in books:
        b.pic_path = b.picture.url[14:]

    try:
        response = paginator.page('page')
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)
    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                      'filters': myFilter,
                      'response': response
                  })


@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = Review.objects.filter(book=book_id)
    book.pic_path = book.picture.url[14:]
    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book,
                      'reviews':reviews
                  })


@login_required(login_url=reverse_lazy('login'))
def mybooks(request):
    books = Book.objects.filter(username=request.user)
    myFilter = BookFilter(request.GET, queryset=books)

    books = myFilter.qs
    paginator = Paginator(books, 5)

    # will grab the current page from the url
    page = request.GET.get('page')

    books = paginator.get_page(page)

    for b in books:
        b.pic_path = b.picture.url[14:]

    try:
        response = paginator.page('page')
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)
    return render(request,
                  'bookMng/mybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                      'filters': myFilter,
                      'response': response
                  })


@login_required(login_url=reverse_lazy('login'))
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request,
                  'bookMng/book_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })

@login_required(login_url=reverse_lazy('login'))
def profile(request):
    books = Book.objects.filter(username=request.user)
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/profile.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  })


@login_required(login_url=reverse_lazy('login'))
def view_reviews(request):
    reviews = Review.objects.all()
    return render(request,
                  'bookMng/view_reviews.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'reviews': reviews
                  })


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


@login_required(login_url=reverse_lazy('login'))
def search_results(request):
    query = request.GET.get('q')
    if query:
        results = Book.objects.filter(
            name__icontains=query
        )
        for b in results:
            b.pic_path = b.picture.url[14:]
    else:
        results = None
    return render(request,
                  'bookMng/search_results.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'results': results,
                  })
