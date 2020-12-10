from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .filters import BookFilter
from .forms import BookForm
from .models import Book, Order
from .models import MainMenu


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


@login_required(login_url=reverse_lazy('login'))
def displaybooks(request):
    books = Book.objects.all()

    # data gets rendered and filters it down if there are any filters applied
    myFilter = BookFilter(request.GET, queryset=books)
    # rebuilds the result from the filter
    books = myFilter.qs

    # pagination for display books, change number of second parameter to get a customized number of books per page
    paginator = Paginator(books, 6)

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
                      'myFilter': myFilter,
                      'response': response
                  })


@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[14:]
    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book
                  })


@login_required(login_url=reverse_lazy('login'))
def mybooks(request):
    books = Book.objects.filter(username=request.user)
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/mybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
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


@login_required(login_url=reverse_lazy('login'))
def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items', '')
        first_name = request.POST.get('firstName', '')
        last_name = request.POST.get('lastName', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '') + " "
        address += request.POST.get('address2', '')
        country = request.POST.get('country', '')
        state = request.POST.get('state', '')
        zipcode = request.POST.get('zip', '')

        order = Order(items=items, first_name=first_name, last_name=last_name, email=email, address=address,
                      country=country, state=state, zipcode=zipcode)
        order.save()
    return render(request,
                  'bookMng/checkout.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      # 'results': results,
                  })
