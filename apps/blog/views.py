from django.shortcuts import render
from .models import Post,Category
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
# from django.shortcuts import render_to_response

# def index (request):
#   return render_to_response('index.html')

def home(request):
  queryset = request.GET.get("search")
  posts = Post.objects.filter(state = True)
  if queryset:
    posts = Post.objects.filter(
      Q(title_icontains = queryset) |
      Q(description_icontains = queryset)
    ).distinct() 

  paginator = Paginator(posts,2)
  page = request.GET.get('page')
  posts = paginator.get_page(page)
  return render(request, 'index.html', {'posts':posts})

def detailPost(request, slug):
  posts = get_object_or_404(Post, slug = slug) 
  return render(request, 'post.html', {'detail_post': posts})

def generals(request):
  queryset = request.GET.get("search")
  posts = Post.objects.filter(
    state = True,
    category = Category.objects.get(name_iexact = 'Generals')
  )
  if queryset:
    posts = Post.objects.filter(
      Q(title_icontains = queryset) |
      Q(description_icontains = queryset),
      state = True,
      category = Category.objects.get(name_iexact = "Generals"),
    ).distinct() 

  paginator = Paginator(posts,2)
  page = request.GET.get('page')
  posts = paginator.get_page(page)
  return render(request, 'generals.html', {'posts':posts})

def news(request):
  posts = Post.objects.filter(
    state = True,
    category = Category.objects.get(name_iexact = 'News')
  ).distinct() 

  paginator = Paginator(posts,2)
  page = request.GET.get('page')
  posts = paginator.get_page(page)
  return render(request, 'news.html', {'posts':posts})

def contact(request):
  posts = Post.objects.filter(
    state = True,
    category = Category.objects.get(name_iexact = 'Contact')
  ).distinct() 

  paginator = Paginator(posts,2)
  page = request.GET.get('page')
  posts = paginator.get_page(page)
  return render(request, 'contact.html', {'posts':posts})