from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Post, Category
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.


#def home(request):
#   return render(request, 'hello.html')


class HomeView(ListView):
    model = Post
    template_name = 'hello.html'
    #ordering = ['-id']  schimb ordinea dar nu e ideal ci mai degraba dupa data
    ordering = ['-post_date','-id']

class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = '__all__'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
   
