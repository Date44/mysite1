from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.core.paginator import Paginator


# auth
def create(request):
    if request.method == 'GET':
        return render(request, 'account/403.html', context={})
    elif request.method == 'POST':
        field_form = PostForm(request.POST, request.FILES)
        field_form.save()
        return redirect('/')


# auth


def details(request, post_id):
    data = dict()
    data['post'] = Post.objects.get(id=post_id)
    return render(request, 'home/details.html', context=data)




def index(request):
    data = dict()  # Словарь данных
    all_posts = Post.objects.all()
    data['posts'] = all_posts

    paginator = Paginator(all_posts, 5)
    page_numder = request.GET.get('page')
    page_obj = paginator.get_page(page_numder)
    data['page_obj'] = page_obj

    return render(request, 'home/index.html', context=data)

